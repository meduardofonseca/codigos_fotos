import SimpleITK as sitk
import os

for p1,s1,f1 in os.walk(r'C:\Users\marco\desktop\mestrado/img_gray'):
    for img1 in f1:
        name1 = img1.split('.JPG')

        im1 = sitk.ReadImage(os.path.join(p1,img1))

        im13d = sitk.JoinSeries(im1)

        sitk.WriteImage(im13d,os.path.join(r'C:\Users\marco\desktop/mestrado/img_gray_nrrd',name1[0] +' nrrd.nrrd'))
  
