import SimpleITK as sitk
import os

for (p1,s1,f1),(p2,s2,f2), (p3,s3,f3) in zip(os.walk(r'c:/users/marco/desktop/mestrado/img_r'),os.walk(r'c:/users/marco/desktop/mestrado/img_g'),os.walk(r'c:/users/marco/desktop/mestrado/img_b')):
    for img1,img2,img3, in zip(f1,f2,f3):
        name1 = img1.split('.JPG')
        name2 = img2.split('.JPG')
        name3 = img3.split('.JPG')
        im1 = sitk.ReadImage(os.path.join(p1,img1))
        im2 = sitk.ReadImage(os.path.join(p2,img2))
        im3 = sitk.ReadImage(os.path.join(p3,img3))
        im13d = sitk.JoinSeries(im1)
        im23d = sitk.JoinSeries(im2)
        im33d = sitk.JoinSeries(im3)
        sitk.WriteImage(im13d,os.path.join(r'c:/users/marco/desktop/mestrado/img_r_nrrd',name1[0]+' nrrd.nrrd'))
        sitk.WriteImage(im23d,os.path.join(r'c:/users/marco/desktop/mestrado/img_g_nrrd',name2[0]+' nrrd.nrrd'))
        sitk.WriteImage(im33d,os.path.join(r'c:/users/marco/desktop/mestrado/img_b_nrrd',name3[0]+' nrrd.nrrd'))


