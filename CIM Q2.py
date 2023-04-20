import bpy
import random

# Generate random values for the box's position, scale, and rotation
pos = [random.uniform(-5, 5) for _ in range(3)]
scale = [random.uniform(0.5, 2) for _ in range(3)]
rot = [random.uniform(0, 360) for _ in range(3)]

# Create a new cube mesh
mesh = bpy.data.meshes.new("BoxMesh")
verts = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
edges = []
faces = [(0, 1, 3, 2), (4, 5, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3), (0, 1, 5, 4), (2, 3, 7, 6)]
mesh.from_pydata(verts, edges, faces)

# Create a new cube object
obj = bpy.data.objects.new("Box", mesh)

# Link the object to the scene collection
collection = bpy.context.scene.collection
collection.objects.link(obj)

# Set the position, scale, and rotation of the box
obj.location = pos
obj.scale = scale
obj.rotation_euler = [radians(rot[i]) for i in range(3)]
