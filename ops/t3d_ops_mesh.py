import bpy, os, sys,  shutil, bpy_extras
from bpy.props import EnumProperty
from bpy.types import PointerProperty, Operator, Header, Menu, Panel, PropertyGroup






class T3D_obj_Props(bpy.types.PropertyGroup):
    project_folder: bpy.props.StringProperty(
        name="Project Folder", description="", subtype="FILE_PATH", default=""
    )

class T3D_OT_UnLoop(bpy.types.Operator):
    """Removes the every other edge loop in the selected loop edges with ctrl + alt + click"""

    bl_idname = "object.t3d_obj_unloop"
    bl_label = "UnLoop"


    def execute(self, context):
        bpy.ops.mesh.select_nth()
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.mesh.dissolve_edges()
    
        return {"FINISHED"}






