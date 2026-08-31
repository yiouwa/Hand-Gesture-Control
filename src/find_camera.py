import cv2

MAX_INDEX_TO_TRY = 5

def try_camera(index: int) -> bool:
    cam = cv2.VideoCapture(index) # Conection to a camara with a index

    if not cam.isOpened():
        print(f"Index {index}: Could not open")
        return False

    print(f"Index {index}: camera opened correctly")
    print("  Press 'n' for the next index, 'q' for quit")

    while True:
        #ret (bool) : True if the frame is took correctly
        ret, frame = cam.read() # request a frame
        if not ret:
            print(f"  iNDEX {index}: not receiving frames")
            break

        # Add text to the frame    
        cv2.putText(frame, f"Camera index: {index}  (n=next, q=quit)",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.imshow("Camera searcher", frame) #show window

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            cam.release()
            cv2.destroyAllWindows()
            return True # Finished all
        elif key == ord("n"):
            break #finished with this camera

    cam.release()
    cv2.destroyAllWindows()
    return False


def main():
    print("Searching available cameras...\n")
    for index in range(MAX_INDEX_TO_TRY):
        if try_camera(index):
            print("\nLeaving.")
            return
    print("\nAll index tested.")


if __name__ == "__main__":
    main()