import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image
from io import BytesIO
import urllib.request


st.markdown(
    f"""
    <h1 style='text-align: center;'>Image Transformation using SVD</h1>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f"""
    <h4 style='text-align: right; text-color: green'>By: Karan Bhardwaj, Sandeep Patel</h4>
    """,
    unsafe_allow_html=True)
st.write("<hr>", unsafe_allow_html=True)



st.subheader("2x2 Matrix Input")

# Create input fields for each element of the matrix
a11 = st.number_input("Enter element (1, 1)", value=3)
a12 = st.number_input("Enter element (1, 2)", value=0)
a21 = st.number_input("Enter element (2, 1)", value=4)
a22 = st.number_input("Enter element (2, 2)", value=5)

# Create a 2x2 matrix using the input values
matrix = np.array([[a11, a12], [a21, a22]])

# Display the matrix
st.subheader("Your Matrix is:")
st.write(matrix)



#Test-1 A unit circle
# Create a unit circle
def unit_circle():
    theta = np.linspace(0, 2*np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    return np.vstack((x, y))


#Test-2 Using URL
def image_api():
    # URL of the image to be read
    url = "data:image/jpeg;base64,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"
    
    # Read the image data from the URL
    image_data = urllib.request.urlopen(url).read()
    # Load the image data into a PIL object
    pil_image = Image.open(BytesIO(image_data))

    # Convert the PIL image to grayscale
    pil_image = pil_image.convert("L")
    circle = np.array(pil_image)
    # Resize the numpy array to a square shape of size 200x200
    return np.resize(circle, (2, 100))

def unit_square(x):
    if abs(x)==1:
        return 0
    else:
        return 1

def square():
    x = np.linspace(-1,1,100)
    y1 = np.vectorize(unit_square)(x)
    y2 = -np.vectorize(unit_square)(x)
    y = np.stack((y1, y2)).flatten()
    x = np.stack((x, x)).flatten()
    return [x,y]

# Test 3 Random matrix
def random_matrix():
    return np.random.rand(2, 100)
    
# Select one of the test image
lst = ['Unit Circle', 'Unit Square','Image through API', 'Random matrix']
selected = st.selectbox("Select image option", lst)
st.subheader(f"You selected:- {selected}")
st.write("<hr>", unsafe_allow_html=True)

functions = [unit_circle, square,image_api, random_matrix]
flag = 0
for i in range(4):
    if lst[i]==selected:
        circle = functions[i]
        if circle == square:
            flag = 1
        break

circle = circle()




# st.title("Image Transformation", text_align = 'center')
st.markdown(
    f"""
    <h1 style='text-align: center;'>Image Transformation</h1>
    """,
    unsafe_allow_html=True
)

# Create a scaling matrix
A = matrix #As input
axis_limit = [-8,8]

# Perform SVD on the scaling matrix
U, s, Vt = np.linalg.svd(A)
horizontal_scale_factor,vertical_scale_factor = s[0], s[1]
clockwise_angle = math.degrees(math.acos(Vt[0][0]))
anticlockwise_angle = math.degrees(math.acos(U[0][0]))
s = np.diag(s)

# Stage 1>>>>> Clockwise rotation
right_rot = Vt @ circle

# Stage 2 >>>>> Horizontal and vertical Scaling
scale_right_rot = s @ right_rot

#Stage 3 >>>>> Anticlock wise rotation
ellipse = U @ scale_right_rot

if flag==0:
    fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(10, 10), subplot_kw={'aspect': 'equal'})
    fig.suptitle('Transformation using SVD')

    # Plot circle
    ax1.plot(circle[0],circle[1])
    ax1.set_xlim(axis_limit)
    ax1.set_ylim(axis_limit)
    ax1.set_title('Stage-1-Original Image')

    # Indicating point P
    x = circle[0, 30]  # x-coordinate of the point
    y = circle[1, 30]  # y-coordinate of the point
    ax1.plot(x, y, 'ro')  # plot the point
    ax1.text(x+0.05, y+0.05, 'P')  # add the label
    # ax1.axis('equal')

    # Indicating Point Q
    x = circle[0, 50]  # x-coordinate of the point
    y = circle[1, 50]  # y-coordinate of the point
    ax1.plot(x, y, 'o',color = 'green')  # plot the point
    ax1.text(x+0.1, y+0.1, 'Q')  # add the label



    # Stage 1>>>> Plot clockwise rotated circle
    ax2.plot(right_rot[0],right_rot[1])
    ax2.set_xlim(axis_limit)
    ax2.set_ylim(axis_limit)
    # ax2.axis('equal')
    ax2.set_title('Stage-2 Clockwise rotation')
    ax2.text(axis_limit[0]+0.4, axis_limit[1]-1, f'Clockwise rotation Angle(in degree) = {clockwise_angle}') 

    # Corresponding point P 
    x = right_rot[0, 30] 
    y = right_rot[1, 30]  
    ax2.plot(x, y, 'ro')  
    ax2.text(x+0.05, y+0.05, 'P') 
    # ax1.axis('equal')

    # Corresponding point Q 
    x = right_rot[0, 50] 
    y = right_rot[1, 50]  
    ax2.plot(x, y, 'o',color = 'green') 
    ax2.text(x+0.1, y+0.1, 'Q')  


    # Stage 2>>>> Horizontal/Verticale scaling
    ax3.plot(scale_right_rot[0],scale_right_rot[1])
    ax3.set_xlim(axis_limit)
    ax3.set_ylim(axis_limit)
    # ax3.axis('equal')
    ax3.set_title('Stage-3 Scaling')
    ax3.text(axis_limit[0]+0.4, axis_limit[1]-1, f'Horizotal Scale factor = { round(horizontal_scale_factor, 2)}')
    ax3.text(axis_limit[0]+0.4, axis_limit[1]-2, f'Vertical Scale factor = { round(vertical_scale_factor, 2)}')

    # # Corresponding point P
    x = scale_right_rot[0, 30] 
    y = scale_right_rot[1, 30]  
    ax3.plot(x, y, 'ro')  
    ax3.text(x+0.05, y+0.05, 'P')  
    # ax1.axis('equal')

    # Corresponding point Q 
    x = scale_right_rot[0, 50]  
    y = scale_right_rot[1, 50]  
    ax3.plot(x, y, 'o',color = 'green')  
    ax3.text(x+0.1, y+0.1, 'Q')  



    # Stage 3>>>>>> Anticlockwise rotation
    ax4.plot(ellipse[0], ellipse[1])
    ax4.set_xlim(axis_limit)
    ax4.set_ylim(axis_limit)
    # ax4.axis('equal')
    ax4.set_title('Stage-4 Anticlockwise rotation')
    ax4.text(axis_limit[0]+0.4, axis_limit[1]-1, f'Anti Clockwise rotation Angle(in degree) = {round(anticlockwise_angle, 2) }')
    # ax4.ylim(-2,2)
    # ax4.show()

    # Corresponding point P
    x = ellipse[0, 30] 
    y = ellipse[1, 30]  
    ax4.plot(x, y, 'ro') 
    ax4.text(x+0.05, y+0.05, 'P')  
    # ax1.axis('equal')

    # Corresponding point Q
    x = ellipse[0, 50] 
    y = ellipse[1, 50]  
    ax4.plot(x, y, 'o',color = 'tab:green')  
    ax4.text(x+0.1, y+0.1, 'Q') 


else:
    fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(10, 10), subplot_kw={'aspect': 'equal'})
    fig.suptitle('Transformation using SVD')

    # Plot circle   
    ax1.plot(circle[0],circle[1], 'r', alpha = 0.5)
    ax1.set_xlim(axis_limit)
    ax1.set_ylim(axis_limit)
    ax1.set_title('Stage-1-Original Image')


    # Stage 1>>>> Plot clockwise rotated circle
    ax2.plot(right_rot[0],right_rot[1], 'r', alpha = 0.5)
    ax2.set_xlim(axis_limit)
    ax2.set_ylim(axis_limit)
    # ax2.axis('equal')
    ax2.set_title('Stage-2 Clockwise rotation')
    ax2.text(axis_limit[0]+0.4, axis_limit[1]-1, f'Clockwise rotation Angle(in degree) = {clockwise_angle}') 


    # Stage 2>>>> Horizontal/Verticale scaling
    ax3.plot(scale_right_rot[0],scale_right_rot[1], 'r', alpha = 0.5)
    ax3.set_xlim(axis_limit)
    ax3.set_ylim(axis_limit)
    # ax3.axis('equal')
    ax3.set_title('Stage-3 Scaling')
    ax3.text(axis_limit[0]+0.4, axis_limit[1]-1, f'Horizotal Scale factor = { round(horizontal_scale_factor, 2)}')
    ax3.text(axis_limit[0]+0.4, axis_limit[1]-2, f'Vertical Scale factor = { round(vertical_scale_factor, 2)}')

    
    # Stage 3>>>>>> Anticlockwise rotation
    ax4.plot(ellipse[0],ellipse[1], 'r')
    ax4.set_xlim(axis_limit)
    ax4.set_ylim(axis_limit)
    # ax4.axis('equal')
    ax4.set_title('Stage-4 Anticlockwise rotation')
    ax4.text(axis_limit[0]+0.4, axis_limit[1]-1, f'Anti Clockwise rotation Angle(in degree) = {round(anticlockwise_angle, 2) }')
    # ax4.ylim(-2,2)
    # ax4.show()




image = st.pyplot(fig)

if st.button('Save Image'):
    # Save the plot to a file
    fig.savefig('saved_plot.png')
    