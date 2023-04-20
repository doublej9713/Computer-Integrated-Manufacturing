# Computer-Integrated-Manufacturing
CIM Q1:This code creates a box mesh with the specified width, height, and depth. It then creates the vertices, edges, and faces of the box using the bmesh module. Finally, it adds the box to the scene and sets its location. You can change the dimensions and location of the box by modifying the values of width, height, depth, and box.location.

CIM Q2:This code first imports the bpy and random modules. Then, it generates random values for the position, scale, and rotation of the box using the random.uniform() method. It creates a new mesh for the box using the from_pydata() method, and creates a new object for the box using the mesh. It links the object to the scene collection using the link() method, and sets the position, scale, and rotation of the box using the location, scale, and rotation_euler attributes of the object.
Note that the radians() function is used to convert the rotation values from degrees to radians
