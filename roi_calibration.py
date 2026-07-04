import cv2

def calibrate_roi(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Could not read from camera.")
        return None

    print("Drag a box around the region you want to watch, then press ENTER or SPACE.")
    print("Press 'c' to cancel selection.")
    roi = cv2.selectROI("Select ROI (native resolution)", frame, showCrosshair=True)
    cv2.destroyAllWindows()

    x, y, w, h = roi
    if w == 0 or h == 0:
        print("No region selected.")
        return None

    frame_h, frame_w = frame.shape[:2]
    # Store as a fraction of the frame, NOT raw pixels
    # This makes the ROI resolution-independent
    normalized_roi = {
        "x": x / frame_w,
        "y": y / frame_h,
        "w": w / frame_w,
        "h": h / frame_h,
    }
    print(f"Selected ROI (normalized): {normalized_roi}")
    return normalized_roi

calibrate_roi(0)