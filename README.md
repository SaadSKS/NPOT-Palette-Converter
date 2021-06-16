# NPOT-Palette-Converter
 Convert NPOT Palette Texture from MagicaVoxel to POT
 
## Requirements:
 - Blender 2.93
 - MagicaVoxel 0.99.6.2
 
## Instructions:
 1. Create/Open your voxel model in MagicaVoxel (Recommended to save your .vox model at this point as well)
 2. In the export tab, select 'OBJ' and export to your preferred location. 3 Files will be created: (sample.obj sample.mtl sample.png)
 3. Now load PaletteMapper.vox in MagicaVoxel 
 4. Import the palette.png that was created in step 2
 5. In the export tab, select '2d' and export to the same location with some new name. (eg: PaletteFixed.png)
 6. Now open up Blender and load PaletteConverter.blend
 7. Import your exported object. File > Import > Wavefront (.obj)
 8. Select the shading tab, and then select your model in the 3D view window
 9. Now in the shader editor window, deselect all nodes and locate the Image Texture node connected to the base color input of the Principled BSDF node
 10. Select 'Open Image' and select the same image from step 5 (eg: PaletteFixed.png)
 11. Select the Scripting tab. The ConvertPalette.py script should already already be imported in the text editor
 12. In the text editor, click 'Run Script'
 13. All Done! You can check in the 3D View Window (with Material Preview) that the UVs have been correctly adjusted to utilize the corrected palette image
