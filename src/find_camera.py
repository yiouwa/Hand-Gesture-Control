import cv2

MAX_INDEX_TO_TRY = 5

def try_camera(index: int) -> bool:
    cap = cv2.VideoCapture(index)

    if not cap.isOpened():
        print(f"Índice {index}: no se pudo abrir")
        return False

    print(f"Índice {index}: cámara abierta correctamente")
    print("  Pulsa 'n' para probar el siguiente índice, 'q' para salir del todo")

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"  Índice {index}: no llegan frames")
            break

        cv2.putText(frame, f"Camara index: {index}  (n=siguiente, q=salir)",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.imshow("Buscador de camara", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            cap.release()
            cv2.destroyAllWindows()
            return True
        elif key == ord("n"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return False


def main():
    print("Buscando cámaras disponibles...\n")
    for index in range(MAX_INDEX_TO_TRY):
        if try_camera(index):
            print("\nSaliendo.")
            return
    print("\nProbados todos los índices.")


if __name__ == "__main__":
    main()