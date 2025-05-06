bl_info = {
    "name": "There LOD Generator",
    "author": "Landminegirl",
    "version": (1, 2),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Custom LOD Tab",
    "description": "Adds a button in the N-Panel to add custom LOD properties to selected objects!",
    "category": "Object",
}

import bpy

# Operator to add custom properties
class OBJECT_OT_add_lod_properties(bpy.types.Operator):
    bl_idname = "object.add_lod_properties"
    bl_label = "Add LOD Properties"
    bl_description = "Add LOD0, LOD1, and LOD2 properties to the selected object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.object
        if obj:
            # Add custom properties to the selected object
            obj["LOD0"] = 75
            obj["LOD1"] = 200
            obj["LOD2"] = 700

            # Force an update to the UI
            obj.update_tag()
            for area in context.screen.areas:
                if area.type == 'PROPERTIES':
                    area.tag_redraw()
            
            self.report({'INFO'}, "LOD properties added to the selected object")
        else:
            self.report({'WARNING'}, "No object selected")
        return {'FINISHED'}

# Panel in the N-Panel (Sidebar)
class OBJECT_PT_custom_lod_panel(bpy.types.Panel):
    bl_label = "Custom LOD Properties"
    bl_idname = "OBJECT_PT_custom_lod_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Custom LOD"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Add Custom LOD Properties:")
        col.operator("object.add_lod_properties", text="Add LOD Properties")

# Register and unregister classes
classes = [
    OBJECT_OT_add_lod_properties,
    OBJECT_PT_custom_lod_panel,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()