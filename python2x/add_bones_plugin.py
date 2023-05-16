import Blender

# Create three bones
bone_names = ["adj", "CHARACTER_REORIENT", "BIP"]

# Get the active armature object
armature = Blender.Object.GetSelected()[0]

# Enter EditMode
Blender.Window.EditMode(1)

# Get the armature data
armature_data = armature.getData()

# Get the root bone of the armature
root_bone = armature_data.bones.values()[0]

# Create the three new bones
bones = []
for name in bone_names:
    bone = Blender.Armature.Editbone()
    bone.name = name
    bones.append(bone)

# Set the parent-child relationships
root_bone_name = root_bone.name

# Set adj as a child of the root bone
bones[0].makeEditable(armature_data)
bones[0].makeParent(root_bone_name)

# Set CHARACTER_REORIENT as a child of adj
bones[1].makeEditable(armature_data)
bones[1].makeParent(bone_names[0])

# Set BIP as a child of CHARACTER_REORIENT
bones[2].makeEditable(armature_data)
bones[2].makeParent(bone_names[1])

# Update the armature
armature_data.update()

# Exit EditMode
Blender.Window.EditMode(0)

print("Bones added successfully!")

