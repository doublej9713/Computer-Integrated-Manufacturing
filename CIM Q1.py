import bpy
import bmesh

# Define the dimensions of the box
width = 2.0
height = 3.0
depth = 1.5

# Create a new mesh and bmesh for the box
mesh = bpy.data.meshes.new("BoxMesh")
bm = bmesh.new()

# Create the vertices of the box
verts = [bm.verts.new((x, y, z)) for x in (-width/2, width/2) for y in (-height/2, height/2) for z in (-depth/2, depth/2)]

# Create the edges of the box
for i in range(0, 8, 2):
    bm.edges.new((verts[i], verts[i+1]))
for i in range(0, 4):
    bm.edges.new((verts[i], verts[i+4]))
for i in range(0, 2):
    bm.edges.new((verts[i], verts[i+6]))

# Create the faces of the box
bm.faces.new((verts[0], verts[2], verts[3], verts[1]))
bm.faces.new((verts[4], verts[5], verts[7], verts[6]))
bm.faces.new((verts[0], verts[1], verts[5], verts[4]))
bm.faces.new((verts[2], verts[6], verts[7], verts[3]))
bm.faces.new((verts[0], verts[4], verts[6], verts[2]))
bm.faces.new((verts[1], verts[3], verts[7], verts[5]))

# Update the bmesh and add it to the mesh
bm.to_mesh(mesh)
bm.free()

# Create an object to hold the box mesh
box = bpy.data.objects.new("Box", mesh)

# Add the box object to the scene
bpy.context.scene.collection.objects.link(box)

# Set the location of the box
box.location = (0, 0, 0)
