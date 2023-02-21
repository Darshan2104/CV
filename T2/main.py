import cv2
import numpy as np
# ==============================================================================
# ==============================================================================
# driving function
def find_potholes(img_path):
    cap = cv2.VideoCapture(path)
    while True:

        # Read the frame
        ret, frame = cap.read()

        # Break the loop if the video has ended
        if not ret:
            break

        # Convert the frame to grayscale
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        blur = cv2.blur(img,(5,5))
        gblur = cv2.GaussianBlur(img,(5,5),0)
        median = cv2.medianBlur(img,5)

        kernel = np.ones((5,5),np.uint8)
        erosion = cv2.erode(median,kernel,iterations = 1)
        dilation = cv2.dilate(erosion,kernel,iterations = 5)
        closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

        edges = cv2.Canny(closing,9,420)

        ret,threshold=cv2.threshold(edges.copy(),0,255,cv2.THRESH_BINARY)
        contours,_=cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    
        # Loop through each contour and pick which satisfy the condition.
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:30]
        for contour in contours:
            # Check if the contour is big enough to be considered a pothole
            if 1500 < cv2.contourArea(contour):
                # Draw a rectangle around the contour
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the frame with the potholes highlighted
        cv2.imshow("Pothole",frame)

        # Break the loop if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture
    cap.release()

    # Close all windows
    cv2.destroyAllWindows()



# ==============================================================================
# ==============================================================================
path = './camera2_road_surface_view.mp4'
find_potholes(path)