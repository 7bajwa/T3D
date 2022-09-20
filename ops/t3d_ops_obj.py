import bpy, os, sys,  shutil, bpy_extras
from bpy.props import EnumProperty
from bpy.types import PointerProperty, Operator, Header, Menu, Panel, PropertyGroup






class T3D_obj_Props(bpy.types.PropertyGroup):
    project_folder: bpy.props.StringProperty(
        name="Project Folder", description="", subtype="FILE_PATH", default=""
    )

class T3D_OT_Grabshot_ref(bpy.types.Operator):
    """It will refress the folder with the copied files"""

    bl_idname = "object.t3d_obj_grabshot_ref"
    bl_label = "Refresh"


    def execute(self, context):
        user_path = bpy.utils.resource_path('USER')
        shot_path = os.path.join(user_path, "grabshots")
        print(shot_path)


        # bpy.ops.export_scene.fbx(user_selection=True,)
    
        return {"FINISHED"}



class T3D_OT_Grabshot(bpy.types.Operator):
    """It will make a copy to paste in other file"""

    bl_idname = "object.t3d_obj_grabshot"
    bl_label = "Grabshot"

    def execute(self, context):
       
        return {"FINISHED"}



