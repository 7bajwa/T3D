from cgitb import text
import bpy, os, sys
from bpy.types import Operator, Header, Menu, Panel, PropertyGroup

from .ops.t3d_ops_misc import (
    T3D_OT_MatVertGroup, 
    T3D_OT_MakeProj, 
    T3D_OT_CopyProject,
    T3D_OT_PurgeData, 
    T3D_OT_STreeFBX, 
    T3D_OT_PackedModel
)

from .ops.t3d_ops_obj import (
    T3D_OT_UnSubdiv,
    # T3D_obj_Props,
    # T3D_OT_Grabshot_ref,
    # T3D_OT_Grabshot
)

from .ops.t3d_ops_mesh import (
    T3D_OT_UnLoop,
)


class T3D_PanelInfo:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "T3D"
    bl_options = {"DEFAULT_CLOSED"}


snap_folder_name = "Grabshots"
this_file_path = os.path.dirname(sys.argv[0])
snap_path = os.path.join(this_file_path,snap_folder_name)

# Making UI for the Baaj tools in the N panel`

class T3D_PT_Tools(T3D_PanelInfo, Panel):
    bl_idname = "T3D_PT_tools"
    bl_label = "Tre3D Tools"

    

    
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.label(text="Misc")
        col.operator(T3D_OT_MatVertGroup.bl_idname, icon="GROUP_VERTEX")
        col.operator(T3D_OT_PurgeData.bl_idname, icon="ORPHAN_DATA")
        col.separator()
        col.label(text="New Folder Setup")
        col.operator(T3D_OT_MakeProj.bl_idname, icon="CURRENT_FILE", text="Create Folder Structure")
        col.operator(T3D_OT_CopyProject.bl_idname, icon="CURRENT_FILE", text="Copy Folder Structure")
        col.separator()
        col.label(text="Import Assets")
        col.operator(T3D_OT_STreeFBX.bl_idname, icon="STRANDS", text="Import Speedtree FBX")
        col.operator(T3D_OT_PackedModel.bl_idname, icon="GROUP", text="Import Zipped Model")

class T3D_PT_Obj(T3D_PanelInfo, Panel):
    bl_idname = "T3D_PT_obj"
    bl_label = "Objects"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator(T3D_OT_UnSubdiv.bl_idname, icon="MESH_GRID")

        return {"FINISHED"}


# class T3D_PT_Obj_Grab(T3D_PanelInfo, Panel):
#     bl_idname = "T3D_PT_obj_grab"
#     bl_label = "Grabshot"
#     bl_parent_id = "T3D_PT_obj"

#     # source_Name: bpy.props.StringProperty(default='Plant_FernIndian')
#     # plant_Name: bpy.props.StringProperty(default='Plant_New')
#     # snap_folder:bpy.props.StringProperty(
#     #     name="Snap Folder", subtype="DIR_PATH", default=snap_path
#     # )
#     # project_folder: bpy.props.StringProperty(name="Project Folder", description="", subtype="FILE_PATH", default="")
#     # source_Name: bpy.props.BoolProperty(default=False)

    
#     def draw(self, context):
#         layout = self.layout
#         row = layout.row(align=True)
#         # row.prop(context.scene, "t3d_snap_folder", text="")
#         row.operator(T3D_OT_Grabshot.bl_idname, icon="SNAP_EDGE", text="Shoot")
#         # row = layout.row(align=True)
#         # row.prop(self, "source_Name")
#         # row.prop(context.scene, "t3d_prop_snaps")
#         # row.operator(T3D_OT_Grabshot_ref.bl_idname, text="", icon="FILE_REFRESH")
#         # row = layout.row(align=True)
#         # row.operator(T3D_OT_Grabshot.bl_idname, icon="IMPORT", text="Grab")

        

class T3D_PT_Mesh(T3D_PanelInfo, Panel):
    bl_idname = "T3D_PT_panel"
    bl_label = "Mesh"

    def draw(self, context):
        layout = self.layout
        # col = layout.column(align=True)
        # col.label(text="Vertex Color Toolkit")
        row = layout.row(align=True)
        row.operator(T3D_OT_UnLoop.bl_idname, icon="SNAP_EDGE")


class T3D_PT_UVS(T3D_PanelInfo, Panel):
    bl_idname = "T3D_PT_uvs_tools"
    bl_label = "UVS"

    
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.label(text="Box Mapping")