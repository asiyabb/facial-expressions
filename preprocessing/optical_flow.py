import cv2

# Function to calculate motion between two images
def compute_flow(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Convert images to grayscale (needed for optical flow)
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calculate optical flow
    flow = cv2.calcOpticalFlowFarneback(
        img1_gray, img2_gray, None,
        0.5, 3, 15, 3, 5, 1.2, 0
    )

    print("Optical flow calculated!")
    return flow

# Test the function
if __name__ == "__main__":
    compute_flow("data/sample/face1.jpg", "data/sample/face2.jpg")
