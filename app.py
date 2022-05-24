import streamlit as st
from PIL import Image

with open("style.css") as f:
  st.markdown(f'<style>{ f.read() }</style>', unsafe_allow_html=True)


#################
# Header
st.write (''' # Muhammad Shahid Mirza. ''')
image = Image.open('shahid-snap-01.jpg')
st.image(image, width=150)

st.markdown('### Summary', unsafe_allow_html=True)
st.info('''
    - Gap Analyst, Internal Auditor and Developer Managment System
    - Working in UAE as QHSE Manager, Internal Auditor from 2010.
    - Data Science learning phase and actively contributor in AI, ML Communities.
''')

#################
# Navigation
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/methoomirza" target="_blank">Shahid Mirza</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#accomplishments">Accomplishments</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#####################
# CUSTOM FUNCTION FOR PRINTING TEXT

def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([2,3,1])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)


#####################
st.markdown('''## Education''')

txt('**Master of Science** (Computer Science), *Virtual University*,  Lahore Pakistan', '')
st.markdown('''
- GPA: `3.62`
- Overall effective CGPA 3.62.
''')

txt('**Bachelors of Science** (Computer Science), *Allama Iqbal Open University*, Islamabad Pakistan', '')
st.markdown('''
- GPA: `60%`
- Graduated with overall 60%.
''')


#####################
st.markdown('''## Work Experience''')
txt('**QHSE Manager, Internal Auditor of Management System**, Consultation and RD Department, Al Sultan Industrial Cement, UAE',
'2010-Present')

st.markdown('''
- Develop, Implement & Review the QHSEMS (Quality, Health & Safety and Environment Management System) with compliance of `ISO 9001:2008, OHSAS 18001:2007 & ISO 14001:2004`.
- Develop the HSE system and maintained to comply the ZonesCorp, IDBA & EAD Abu Dhabi requirements.
- Maintain document, implement, and continual improvement of the systems.
- GAP Analysis to ensure the implementation of management systems.
- Communicate 3rd party to conduct the Trainings.
- Up-gradation and Integration of OSHAD and QHSE-MS `(ISO 9001:2008, 14001:2004, BS 18001:2007) Management System to IMS (ISO 9001:2015, 14001:2015, 45001:2018 & OSHAD Framework V3.1)`.
''')

txt('**Kaglgle Expert/Freelancer**, Data Science & Analysis, Kaggle Data Science Company, Online Data Science Community', '2021-Present')
st.markdown('''
- Kaggle: is a subsidiary of Google LLC, is an online community of data scientists and machine learning practitioners.
- Kaggle allows users to find and publish data sets, explore and build models in a web-based data-science environment.
- Allow to work with other data scientists and machine learning engineers
- Participate in competitions to solve data science challenges.
''')

txt('**Web Developer**, PHP Programmer, Affordable Programmer, Online-Canada', '2019-2010')
txt('**Data Processor**, District Coordination Offfice, Government of Punjab, Pakistan', '2006-2010')
txt('**Lecturer**, Faculty of Computer Science, Peak Solution Institute, Lahore Pakistan', '2003-2004')


#####################
st.markdown('''## Certifications''')
txt('**Lead Auditor, 9001:2015**, IRCA Certified, - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -Certification #: EDU/QMS/LA/18/03213', '2018-Present')
txt('**Lead Auditor, 45001:2018**, IRCA Certified, - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Certification #: EDU/OHSMS/LA/18/02346', '2018-Present')
txt('**ITIL Foundation**, Information Technology Infrastructure Library, - - - - - - - - - - - - Certification #: 03604736-01-24TT', '2015-Present')
txt('**Microsoft Technology Associate**, MTA - [ Networking Fundamental ], - - - - - - - - Certification #: F282-2026', '2015-Present')


#####################
st.markdown('''## Accomplishments''')
txt4('Introduction to Python', '`DataCamp` Accomplish Statement, provide basic knowledge of Python and libraries that help in Data Science.', 'https://www.datacamp.com/statement-of-accomplishment/course/433484b6f7c8e9fa9a46e786c85b28ab29f9c37c')
txt4('Python For Data Science', '`Dataquest` it provides the basic Python Foundation for Data Science like `Variables, Data Types and Lists in Python`.', 'https://app.dataquest.io/verify_cert/GQN5V8LIM18MR46WFMBX/')
txt4('Python For Data Science', '`Dataquest` learn the Loop and Conditional Statements of Python, Hand-on Experience how to use in real-life of Data Science.', 'https://app.dataquest.io/verify_cert/969LG7BXW0AH2RD9LV1E/')
txt4('Data Analysis with Python', 'Powered by `IBM` Acknowledges achievements certificates, are awarded for knowledge, skill and abilities to perform Data Analyst role.', 'https://www.credly.com/go/mJLsTCrU')
txt4('Python for Data Science', 'Powered by `IBM` it helpful me for basic knownledge of Python and Data Science with Hand-on Experience', 'https://www.credly.com/go/4z0EdVcy')
txt4('Data Visualization with Python', 'Powered by `IBM` A computational tool for the prediction and analysis of anticancer peptides','https://www.credly.com/go/gFZSM4of')
txt4('Data Data, Everywhere', '`Coursera` Foundation Data Data, Everywhere: Define key concepts in data analytics including data, data analysis, and data ecosystem', 'https://coursera.org/verify/8YAF8RBC38NN')
txt4('Feature Engineering', '`Kaggle` This course helped to understand how feature engineering improves the overall score of machine learning models and how to process the features.', 'https://www.kaggle.com/learn/certification/methoomirza/feature-engineering')


#####################
st.markdown('''## Skills''')
txt3('Programming', '`Python`, `R`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Web development', '`HTML`, `CSS`, `PHP`, `ASP`, `AJAX`, `Java-Script`, `VB-Script`, `JQuery`')


#####################
st.markdown('''## Social Media''')
txt2('LinkedIn', 'https://www.linkedin.com/in/shahid-mirza-71ba56166')
txt2('Twitter', 'https://twitter.com/methoomirza')
txt2('GitHub', 'https://github.com/methoomirza')
txt2('DagsHub', 'https://dagshub.com/methoomirza')