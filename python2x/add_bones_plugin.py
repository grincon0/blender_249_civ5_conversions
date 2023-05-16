import Blender

# Create three bones
bone_names = ["adj", "CHARACTER_REORIENT", "BIP"]

# Get the active armature object
armature = Blender.Object.GetSelected()[0]
armature.makeEditable()

# Get the root bone of the armature
root_bone = armature.getData().bones.values()[0]

# Create the three new bones
bones = []
for name in bone_names:
    bone = Blender.Armature.Editbone()
    bone.name = name
    bones.append(bone)

# Set the parent-child relationships
root_bone_name = root_bone.name

# Set adj as a child of the root bone
bones[0].parent = root_bone_name

# Set CHARACTER_REORIENT as a child of adj
bones[1].parent = bone_names[0]

# Set BIP as a child of CHARACTER_REORIENT
bones[2].parent = bone_names[1]

# Update the armature
armature.update()
armature.makeDisplayList()

# Switch back to object mode
Blender.Scene.GetCurrent().update()

print("Bones added successfully!")
