import matplotlib.pyplot as plt 
import matplotlib.patches as patches
import matplotlib.animation as animation 
import numpy as np 
plt.style.use('dark_background')

fig = plt.figure() 
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50)) 
line, = ax.plot([], [], lw=2) 

conversion_factor = 180/np.pi
width, height = 10.0, 6.0
x, y, theta = 0.0, 0.0, 0.0 # (x, y, theta)
car = patches.Rectangle(xy=(x + width/2, y+height/2), width=width, height=height, 
						angle=conversion_factor*theta,rotation_point='center', fc='b')
ax.add_patch(car)

# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	car.set_xy((x-width/2,y - height/2))
	car.angle = conversion_factor * theta
	return line, car

# lists to store x and y axis points 
xdata, ydata = [], [] 

# animation function 
def animate(i): 
	global x, y, theta
	dt = 0.1 # time-step
	v = 2 # velocity
	w = (np.pi/180) * 6 # ANGULAR velocity
	
	# Update state	
	theta +=  w * dt 
	x +=  v * np.cos(theta) * dt
	y +=  v * np.sin(theta) * dt

	# Update car position and orientation
	car.set_xy((x - (width/2), y - (height/2)))
	car.angle = conversion_factor * theta

	# Update trail
	xdata.append(x) 
	ydata.append(y) 
	line.set_data(xdata, ydata) 

	return line, car
	
# setting a title for the plot 
plt.title('Dubins model') 
# hiding the axis details 
plt.axis('off') 

# call the animator	 
anim = animation.FuncAnimation(fig, animate, init_func=init, 
							frames=700, interval=20, blit=True) 

# save the animation as mp4 video file 
anim.save('coil.mp4',writer='ffmpeg', fps=30)  
