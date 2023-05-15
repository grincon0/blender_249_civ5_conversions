bl_info = {
    "name": "Add Civ 5 Bones",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 4, 9),
    "location": "View3D > Tool Shelf > Add Bones",
    "description": "Adds three bones to the base of the armature",
    "category": "Rigging"
}

import bpy


def add_bones_to_armature(context):
    # Get the active object (assuming it's an armature)
    armature = context.active_object

    # Get the root bone of the armature
    root_bone = armature.data.bones[0]  # Assumes the root bone is the first bone in the armature

    # Create the three new bones
    bone_names = ["adj", "CHARACTER_REORIENT", "BIP"]
    bones = []

    for name in bone_names:
        bone = armature.data.edit_bones.new(name)
        bones.append(bone)

    # Set the parent-child relationships
    root_bone_name = root_bone.name

    # Set adj as a child of the root bone
    bones[0].parent = root_bone
    bones[0].use_connect = True

    # Set CHARACTER_REORIENT as a child of adj
    bones[1].parent = bones[0]
    bones[1].use_connect = True

    # Set BIP as a child of CHARACTER_REORIENT
    bones[2].parent = bones[1]
    bones[2].use_connect = True

    # Update the armature
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.view_layer.update()


class AddBonesOperator(bpy.types.Operator):
    bl_idname = "object.add_bones"
    bl_label = "Add Civ 5 Bones"
    bl_description = "Adds three bones to the base of the armature"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        add_bones_to_armature(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(AddBonesOperator.bl_idname, text="Add Bones")


def register():
    bpy.utils.register_class(AddBonesOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(AddBonesOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
