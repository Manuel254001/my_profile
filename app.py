from PIL import Image

import requests
import streamlit as st
from streamlit_lottie import st_lottie

# find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="my webpage", page_icon=":tada", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
## use local css
# noinspection PyPackageRequirements
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

#load ....assets....


lottie_coding = load_lottieurl("https://lottie.host/432273ac-4283-46d3-ab90-65f1db1d5f9d/XMEAfISR4j.json")
img_contact_form = Image.open("yt_contact_form.png.png")
img_lottie_animation = Image.open("yt_lottie_animation.png.png")





#.... HEADER SECTION......
with st.container():
     st.subheader("Hi, I am Emmanuel Muthomi Muchui:wave:")
     st.title("An Accountant from Kenya")
     st.write("Accounting isn't just a profession to me; it's a passion that ignites my curiosity "
              "and drives my dedication. From the meticulous process of balancing ledgers to the strategic analysis of financial data, I find joy in unraveling the intricacies of financial management. What truly captivates me, however, is the transformative power of accounting software. These technological marvels not only streamline mundane tasks but also empower businesses to make data-driven decisions with precision and agility. The ability to harness the capabilities of accounting software fuels my enthusiasm, as I immerse myself in exploring their functionalities and leveraging their potential to optimize financial processes. To me, accounting software isn't just a tool; it's a gateway to efficiency, accuracy, and innovation in the realm of financial management.")
     st.write("[Learn More >](https://www.linkedin.com/in/emmanuel-muthomi-5816322aa)")

#..what i do...
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what i do")
        st.write("##")
        st.write(
        """
    
        >I am an accountant with a Multifaceted Skillset
        While I'm currently honing my accounting skills in the classroom, my passion for the field extends far beyond textbooks.
         
         >I envision myself as a meticulous and analytical accountant, meticulously tracking financial data, ensuring its accuracy, and preparing timely reports. This could involve tasks like managing accounts payable and receivable, bookkeeping, or creating financial statements.
        My true strength lies in combining my accounting knowledge with my diverse skillset.
        
        >My sharp data analysis abilities allow me to interpret financial trends and identify areas for improvement.Additionally, my strong communication skills, honed through online writing and social media marketing, ensure clear and concise financial reports that resonate with both internal and external stakeholders.
        Furthermore, my graphic design skills can be a valuable asset when creating clear and visually appealing financial presentations.
        
       > This bridges the gap between data and understanding, making complex information more accessible.
        Beyond technical skills, my experience as a peer counselor demonstrates my ability to explain complex topics in a relatable way.This is invaluable when communicating financial concepts to colleagues or clients.My passion for social responsibility extends beyond the financial realm.As a current peer counselor, an ADA drug educator, and an environmentalist, I am committed to creating a positive impact.This well-rounded perspective allows me to see the bigger picture of how financial decisions affect stakeholders and the environment.
        In essence, I bring more than just a passion for accounting to the table.I offer a unique blend of skills and experiences that make me a valuable asset in any accounting role.
     """
        )
        st.write("[Facebook page>](https://www.facebook.com/profile.php?id=100052271172231&mibextid=ZbWKwL)")

    with right_column:
     st_lottie(lottie_coding, height=900, key="coding")

     #####....projects...
     with st.container():
         st.write("---")
         st.header("My projects")
         st.write("##")
         image_column, text_column = st.columns((1, 2))
         with image_column:
             st.image(img_lottie_animation)
             st.empty()
     with text_column:

         st.subheader(" Accurate and Transparent Reporting: Leveraging IFRS for Financial Statement Preparation")
         st.write("##"
        
             """
Skills Used: Financial Analysis, Data Visualization (Tableau/Excel), Investment Research
             Description:
Selection of a specific industry and analyze publicly available financial statements of several companies within that sector. Employ in-depth financial analysis, incorporating advanced ratios and metrics (e.g., DuPont analysis, free cash flow analysis) to identify investment opportunities.
Utilize data visualization tools (Tableau, Excel) to create compelling presentations of your findings.
>Accounting Relevance:

>Financial statement analysis is essential for evaluating a company's financial health, risks, and investment potential.
Advanced ratios and metrics provide deeper insights into profitability, liquidity, solvency, and efficiency.
             
             
             
             """

     )
         st.markdown("[My Recent Analysis...](https://eu.docworkspace.com/d/sIPrJzdnXAfiTjrIG)")

         with left_column:
             st_lottie(lottie_coding, height=900,)

with st.container():
    Image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
        with text_column:
            st.subheader("Emmanuel's Tax Efficiency Project")
            st.write(
                """
                This photo represents my volunteer experience assisting low-income families with tax preparation. During this project, I utilized my knowledge of tax regulations and data entry skills to ensure accurate and efficient tax filing for my clients. I also honed my communication skills by explaining complex tax concepts in simple terms.
                """

            )
            st.markdown("[My x showing my interest with working with organizations...](https://twitter.com/Manuel254001/status/)")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
   ###<form action="https://**correct_form_submission_url**" method="POST">
#</form>
    contact_form = """
   <form action="https://formsubmit.co/manuelgold254@email.com" method="POST"> 
</form>

   
   <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "Your name" required>
     <input type="email" name="email" placeholder= "Your email address" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
       st.empty()



             


