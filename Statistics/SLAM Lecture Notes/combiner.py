#This file implements a combining algorithm for all the pdfs in this folder

from PyPDF2 import PdfReader, PdfWriter


paths = ['/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/01-ECEN633-F23-Introduction.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/02-ECEN633-ProbReview-Basics.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/03-ECEN633-RigidBodyTransformations.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/04-ECEN633-BayesFilters.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/05-ECEN633-OccupancyGridMapping.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/06-ECEN633-ProbReview-Gaussians.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/07-ECEN633-ProbReview-Uncert-Propagation.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/08-ECEN633-ParticleFilters.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/09-ECEN633-ParticleFilterLocalization.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/10-ECEN633-IntroKalmanFiltering.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/11-ECEN633-KF-Notes.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/12-ECEN633-EKF.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/13-ECEN633-UnscentedTrans-UKF.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/14-ECEN633-Lab4-EKF-UKF-Localization-Notes.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/15-ECEN633-EKF-SLAM (1).pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/16-ECEN633-Lab5-EKF-SLAM-Notes (1).pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/17-ECEN633-Cameras.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/18-Lidar and Scan Matching.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/19-Additional_LiDARandScanMatching.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/20-ECEN633-Least-Squares-Notes.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/21-ECEN633-Intro-Factor-Graph-SLAM.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/22-Michael-SLAM-as-MLE-Notes.pdf',
         '/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/23-ECEN633-Factor-Graph-SLAM-Continued.pdf']


#creates the writer
merger = PdfWriter()

for pdf in paths:
    merger.append(pdf)

merger.write("/home/dben1182/Documents/useful-textbooks/Statistics/SLAM Lecture Notes/SLAM_Complete_Notes.pdf")
merger.close()