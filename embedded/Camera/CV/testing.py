import streamlit as st
import urllib.request
import cv2
import numpy as np



url = 'http://192.168.1.9/getFrames.jpg'
# Set page title
st.set_page_config(page_title="Image Editor", page_icon=":pencil2:")

# Define function to apply a filter to the image
def apply_filter(image):
    da=image
    da=cv2.resize(da,(800,800))
    darts=cv2.resize(image,(800,800))
    img=darts
    image=darts
    blur1 = cv2.GaussianBlur(image, (5,5), 0) 

    # blur1 = cv2.GaussianBlur(img, (3, 3),0)
    # median = cv2.medianBlur(gray, 3)
    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(blur1, cv2.COLOR_BGR2HSV)

    # Define range of green color
    green_lower = (25, 40, 0)
    green_upper = (100, 255, 255)

    # Create a binary mask that marks the pixels corresponding to the object
    mask_green = cv2.inRange(hsv_image, green_lower, green_upper)


    # Apply the mask to the original image to extract the object
    # object = cv2.bitwise_and(image, image, mask=mask)

    # Define range of red color
    bag_lower = (15, 30, 180)
    bag_upper = (25, 70,255 )
    bag_lower2 = (0, 50, 200)
    bag_upper2 = (230, 90, 255) 
    # Create a binary mask that marks the pixels corresponding to the object
    mask2= cv2.inRange(hsv_image, bag_lower, bag_upper)
    mask3 = cv2.inRange(hsv_image, bag_lower2, bag_upper2)
    mask_bag = cv2.bitwise_or(mask2, mask3)

    # Define range of red color
    red_lower = (0, 50, 50)
    red_upper = (10, 255, 255)
    red_lower2 = (170, 50, 50)
    red_upper2 = (180, 255, 255)

    # Create a binary mask that marks the pixels corresponding to the object
    mask1r = cv2.inRange(hsv_image, red_lower, red_upper)
    mask2r = cv2.inRange(hsv_image, red_lower2, red_upper2)
    mask_red = cv2.bitwise_or(mask1r, mask2r)

    # Define range of black color
    black_lower = (0, 0, 0)
    black_upper = (170, 90,130)

    # Create a binary mask that marks the pixels corresponding to the object
    mask_black = cv2.inRange(hsv_image, black_lower, black_upper)


    mask=  mask_bag + mask_green+ mask_red + mask_black
    # Apply the mask to the original image to extract the object
    mas = cv2.bitwise_and(image, image, mask=mask)
    image=image-mas


    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # m=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # plt.imshow(m,'gray')
    blur1 = cv2.GaussianBlur(gray, (5, 5), 0)
    median = cv2.medianBlur(gray, 3)

    _, thresh = cv2.threshold(median, 150, 200, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    # Perform erosion
    eroded = cv2.erode(thresh, kernel)

    # Perform opening (erosion followed by dilation)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Perform closing (dilation followed by erosion)

    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # Perform dilation
    # dilated = cv2.dilate(opening, kernel)


    # Display the results of morphological operations
    # cv2.imshow('Dilated', dilated)

    # cv2.imshow('Eroded', eroded)
    # cv2.imshow('Opening', opening)
    # cv2.imshow('Closing', closing)

    canny2 = cv2.Canny(opening, 200, 250)
    # cv2.imshow('canny2',canny2)



    scoress=[]
    # Get the image height and width
    height, width = img.shape[:2]
    height= height+20
    width = width-5
    z=0
    y=0
    # Get the center of the image
    center = (width // 2, height // 2)
    # center[0] =center[0] -2
    # center[1]=center[1]-2
    # Draw the x-y axis
    cv2.line(img, (center[0], 0), (center[0], height), (0, 255, 0), 2)
    cv2.line(img, (0, center[1]), (width, center[1]), (0, 255, 0), 2)




    # Find the contours of the shape
    contours, _ = cv2.findContours(canny2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # # Get the center point of the image
    # height =height-20
    # width =width- 2
    center_point = np.array([int(width/2), int(height/2)])

    # Loop through all the contours and find the nearest point
    for contour in contours:
        # Find the nearest point to the center point of the image
        distances = []
        for point in contour:
            dist = cv2.norm(np.subtract(center_point, point[0]))
            distances.append(dist)
        nearest_point_index = np.argmin(distances)
        nearest_point = tuple(contour[nearest_point_index][0])

        # Draw a line from the center point to the nearest point in the contour
        # cv2.line(img, tuple(center_point), nearest_point, (0, 0, 255), 2)








    # import cv2
    # import numpy as np
    # import random

    # img_=cv2.imread('7.png')
    # img=np.copy(img_)
    # img=cv2.resize(img,(800,800))


        # Generate a random point
        x = nearest_point[0]
        y = nearest_point[1]
        cv2.line(img, center, (x,y), (0, 255, 0), 2)
        # Draw the point
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        y+=25
        # Calculate the difference between the point and the center
        dx = x - center[0]
        dy = center[1] - y

        # Calculate the angle
        if dx == 0:
            if dy > 0:
                angle = 90
            else:
                angle = 270
        else:
            angle = np.arctan(dy/dx) * 180 / np.pi
            if dx < 0: 
                angle += 180 
            elif dy <0 :
            # else:
                angle += 360
        # Show the angle
        # print("Angle:", angle, "degrees")

        # Map the angle to the corresponding sector on the dartboard
        if angle >= 81 and angle <= 99:
            score = 20
        elif angle >= 63 and angle <= 80:
            score = 1
        elif angle >= 45 and angle <=62:
            score = 18
        elif angle >= 27 and angle <=44:
            score = 4
        elif angle >=9 and angle <= 26:
            score = 13
        elif angle >= 351 and angle <=8:
            score = 6
        elif angle >= 333 and angle <= 352:
            score = 10
        elif angle >= 315 and angle <= 332:
            score = 15
        elif angle >= 297 and angle <=314:
            score = 2
        elif angle >= 279 and angle <= 298:
            score = 17
        elif angle >= 261 and angle <= 278:
            score = 3
        elif angle >= 243 and angle <= 260:
            score = 19
        elif angle >= 225 and angle <= 242:
            score = 7
        elif angle >= 207 and angle <=224:
            score = 16
        elif angle >= 189 and angle <= 206:
            score = 8
        elif angle >= 171 and angle <= 188:
            score = 11
        elif angle >= 153 and angle <= 170:
            score = 14
        elif angle >= 135 and angle <= 152:
            score = 9
        elif angle >= 117 and angle <= 134:
            score = 12
        elif angle >= 99 and angle <=116:
            score = 5


        # Calculate the length of the line
        line_length = ((x - center[0])**2 + (y - center[1])**2)**0.5
        linee=round(line_length)
        if (linee) >= 230 and linee <=240:
            score=score*2

        # Put the angle on the image
        cv2.putText(da, f"score: {score:} ", ( 15, 15+z),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        scoress.append(score)
        z+=20
        # Calculate the length of the line
        # line_length = ((x - center[0])**2 + (y - center[1])**2)**0.5

        


    return da

# Define Streamlit app
def app():
    # Set app title
    st.title("Image Editor")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    # If image is uploaded
    if uploaded_file is not None:
        # Read image using OpenCV
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        original_image = cv2.imdecode(file_bytes, 1)

        # Display original image
        st.image(original_image, channels="BGR", caption="Original Image", use_column_width=True)

        # Choose a filter to apply to the image
        # filter_name = st.selectbox("Choose a filter", ["None", "Blur", "Grayscale", "Canny"])

        # Apply filter and display edited image
        edited_image = apply_filter(original_image)
        st.image(edited_image, channels="BGR", caption="Edited Image", use_column_width=True)

    while True:
        cap = urllib.request.urlopen(url)
        image = np.asarray(bytearray(cap.read()), dtype="uint8")
        frame = cv2.imdecode(image, cv2.IMREAD_COLOR)  # Replace with your camera sourceq
        detected_frame = apply_filter(frame)
        cv2.imshow("DartsSense", detected_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

# Run Streamlit app
if __name__ == "__main__":
    app()