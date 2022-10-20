from pypylon import pylon
import platform

num_img_to_save = 5
img = pylon.PylonImage()
tlf = pylon.TlFactory.GetInstance()

cam = pylon.InstantCamera(tlf.CreateFirstDevice())
cam.Open()
cam.GainAuto.SetValue("Once")
cam.StartGrabbing()

for i in range(num_img_to_save):
    with cam.RetrieveResult(2000) as result:

        img.AttachGrabResultBuffer(result)

        if platform.system() == 'Windows':
            
            ipo = pylon.ImagePersistenceOptions()
            
            quality = 100
            ipo.SetQuality(quality)

            filename = "saved_pypylon_img_%d.bmp" % quality
            img.Save(pylon.ImageFileFormat_Bmp, filename)
        else:
            filename = "saved_pypylon_img_%d.png" % i
            img.Save(pylon.ImageFileFormat_Png, filename)

        img.Release()

cam.StopGrabbing()
cam.Close()