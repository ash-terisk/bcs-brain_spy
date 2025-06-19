A.  AFFINE MATRIX and Orientation Tags :

1. The affine matrix in NIfTI file is used to convert a voxel coordinate system to a RAS+ coordinate system or vice versa.
2. [x, y, z, 1] = affine @ [i, j, k, 1] where (x,y,z) is in RAS and (i,j,k) is in voxel.
3. The orientaion tag in DICOM files is another way of denoting the orientaion in real world of axes with respect to image.
4. The format is (cosine vectors of row, cosine vectors of column).
5. We can also convert the orientation tags into affine matrix and it work in the same way as it works in NIfTI file.
6. Due to unavalability of a suitable dataset, the dataset used in the given directory has scans from all orientations in the dataset.
This kind of dataset is not suitable for using the affine matrix.


B. Understanding Orientation Matrix :

+X	Patient's left to right
+Y	Posterior to anterior
+Z	Inferior to superior

So the orientation matrix tells us:

Which way is left/right (x),

Which way is front/back (y),

Which way is up/down (z).


c. DICOM vs NIfTI — Key Differences

1. Intended Use
- DICOM: Primarily used in CLINICAL environments such as hospitals and radiology departments. It supports PACS (Picture Archiving and Communication Systems), reporting, and archiving workflows.
- NIfTI: Designed for RESEARCH, especially in neuroimaging (e.g., fMRI, MRI, DTI). Widely used in brain imaging research and analysis pipelines.

2. File Formats
- DICOM: Usually one file per image slice. A typical scan may consist of hundreds of `.dcm` files.
- NIfTI: Encapsulates the entire volume in a single `.nii` or compressed `.nii.gz` file, making it easier to manage.

3. Metadata Structure
- DICOM: Rich and hierarchical. Contains thousands of standardized fields (tags), including patient info, scan settings, timestamps, and equipment details.
- NIfTI: Contains a simpler, flat header structure. Metadata is focused on what’s needed for analysis: affine, shape, data type, etc.

4. Ease of Use and Tooling in Python
- DICOM: Comparatively tougher to work with as there are discrete scans which have to be stacked together. 
- NIfTI: Easy to use with `nibabel`.

5. Spatial Orientation and Affine
- DICOM: Orientation must be calculated using `ImagePositionPatient` and `ImageOrientationPatient` which can then be converted to affine matrix.
- NIfTI: Includes an affine matrix directly in the header for mapping voxel indices to real-world coordinates.

Summary
DICOM is useful for clinical workflows, as it contains less slices (but all which are important). It also contains important information for medical analysis like patient information, date of imaging etc.
NIfTI is simpler, research-friendly and much more useful for data training as the slices are compact.


D. Orientation Handling Comparison:

1. Format:
   - DICOM: Multiple 2D slices with metadata.
   - NIfTI: Single 3D/4D volume with embedded spatial info.

2. Orientation Definition:
   - DICOM: Uses ImageOrientationPatient (6 direction cosines) and ImagePositionPatient.
   - NIfTI: Uses a 4×4 affine matrix in the header.

3. Coordinate System:
   - DICOM: Patient-based (L→R, P→A, F→H).
   - NIfTI: Usually RAS (Right, Anterior, Superior) or LPS.

4. Slice Order:
   - DICOM: Must be sorted manually using metadata.
   - NIfTI: Defined implicitly by the affine matrix.