import streamlit as st
from datetime import datetime, timedelta
import googlemaps
import os
from streamlit_extras.card import card 
import pandas as pd
import urllib.parse


# Set page config
st.set_page_config(
    page_title="Naari - Women's Essentials",
    page_icon="🌸",
    layout="wide"
)

# Dictionary to map pages to their content functions
PAGES = {
    "About Us & Helpline": "about",
    "Self Defense": "self_defense",
    "Menstrual Health": "menstrual",
    "Gynecologist Finder": "gynecologist",
    "Know Your Rights": "rights",
}

# Define page content functions
def about_page():
    st.header("About Naari")
    st.write("""
    Welcome to Naari, a project born from passion, purpose, and the unwavering belief 
    in creating a safer world for women. We are a team of four young women pursuing 
    our Master's in Informatics, united by a shared dream: to use technology as a 
    tool for empowerment and change.
    """)
    
    # Helpline Section
    st.header("Emergency Helplines")
    helplines = {
        "Women Helpline (All India)": "1091",
        "Police (Emergency)": "100",
        "Domestic Violence Helpline": "181",
        "National Commission for Women": "011-26942369",
        "Childline (For Children)": "1098"
    }
    
    for name, number in helplines.items():
        with st.expander(f"{name}: {number}"):
            st.write(f"Service: {name}")
            st.write(f"Call: {number}")
            if st.button(f"Call {number}", key=number):
                st.write(f"📞 Calling {number}...")

def self_defense_page():
    st.title("Self-Defense Techniques and Tools")
    
    # Create tabs
    tab1, tab2 = st.tabs(["Techniques", "Tools"])

    with tab1:
        st.header("Empower Yourself: Self-Defense Techniques for Women")
        st.image("https://via.placeholder.com/800x400", caption="Self Defense Techniques")
        
        st.write("""
        A study from the University of Oregon found that women who took self-defense classes felt safer, 
        more confident, and more empowered. To help you feel more secure, here are some essential 
        self-defense techniques:
        """)
        
        # Vulnerable Areas Section
        st.subheader("Focus on Vulnerable Areas")
        st.image("https://via.placeholder.com/800x400", caption="Vulnerable areas to target")
        st.write("""
        When defending yourself, aim for your attacker's most vulnerable spots:
        - **Eyes:** A forceful poke can temporarily blind them
        - **Nose:** A strong strike can cause severe pain and bleeding
        - **Throat:** A firm strike can disrupt breathing
        - **Groin:** A well-placed kick can incapacitate an attacker
        """)
        
        # Avoid Targets Section
        st.subheader("Avoid Less Effective Targets")
        st.write("""
        Avoid aiming for the chest or knees, as these areas are less sensitive and may not be 
        as effective in deterring an attacker.
        """)
        
        # Force and Voice Section
        st.subheader("Maximize Your Force and Voice")
        st.write("""
        Use all your strength and aggression during a self-defense situation. 
        Yelling loudly can intimidate an attacker and attract attention.
        """)
        
        # Key Moves Section
        st.subheader("Key Self-Defense Moves")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("""
            - **Hammer Strike:** Use your keys as a weapon
            - **Groin Kick:** Powerful kick to incapacitate
            - **Heel Palm Strike:** Aim for nose or throat
            - **Elbow Strike:** Powerful blows to head/neck
            """)
        
        with col2:
            st.write("""
            - **Escape from Bear Hug:** Bend forward and use elbows
            - **Escape with Hands Trapped:** Strike groin and turn
            - **Escape from Side Headlock:** Strike groin to escape
            """)
        
        # Safety Tips Section
        st.subheader("Additional Safety Tips")
        st.write("""
        - **Stay Aware:** Be mindful of your surroundings
        - **Set Boundaries:** Clearly communicate your limits
        - **Carry Tools:** Consider pepper spray or personal alarm
        - **Practice:** Enroll in a self-defense class
        """)
        
        st.write("""
        Remember, self-defense is about empowering yourself and taking control of your safety. 
        By learning these techniques and staying alert, you can increase your confidence and 
        reduce your risk.
        """)

    with tab2:
        st.header("Self-Defense Tools: A Quick Guide")
        
        # Pepper Spray
        with st.expander("Pepper Spray", expanded=True):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image("https://via.placeholder.com/300x150", caption="Pepper Spray")
            with col2:
                st.write("**How to use:** Aim for the attacker's face, avoiding wind direction")
                
                st.subheader("Advantages:")
                st.write("""
                - Effective deterrent
                - Non-lethal
                - Easy to carry
                """)
                
                st.subheader("Disadvantages:")
                st.write("""
                - Limited range
                - Affected by wind
                - May cause temporary discomfort
                """)
                
            st.write("[Amazon](https://www.amazon.com) | [Flipkart](https://www.flipkart.com)")
        
        # Personal Alarm
        with st.expander("Personal Alarm"):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image("https://via.placeholder.com/300x150", caption="Personal Alarm")
            with col2:
                st.write("**How to use:** Pull the pin or press the button to activate loud alarm")
                
                st.subheader("Advantages:")
                st.write("""
                - Draws attention
                - Easy to carry
                - Can deter attackers
                """)
                
                st.subheader("Disadvantages:")
                st.write("""
                - Less effective in noisy areas
                - Relies on others noticing
                """)
                
            st.write("[Amazon](https://www.amazon.com) | [Flipkart](https://www.flipkart.com)")
        
        # Stun Gun
        with st.expander("Stun Gun"):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image("https://via.placeholder.com/300x150", caption="Stun Gun")
            with col2:
                st.write("**How to use:** Aim prongs at attacker's body and press trigger")
                
                st.subheader("Advantages:")
                st.write("""
                - Temporarily incapacitates
                - Easy to use
                - Portable
                """)
                
                st.subheader("Disadvantages:")
                st.write("""
                - Requires direct contact
                - Legal restrictions may apply
                """)
                
            st.write("[Amazon](https://www.amazon.com) | [Flipkart](https://www.flipkart.com)")
        
        st.info("""
        **Note:** While self-defense tools can be helpful, the best defense is often awareness, 
        avoidance, and self-defense training. Always prioritize your safety and seek professional 
        training if possible.
        """)

# Add other page functions (you can fill these in later)
def menstrual_page(): 
    st.title("Menstrual Health & Cycle Tracker")
    
    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Cycle Guide", "Product Guide", "Cycle Tracker"])
    
    with tab1:
        st.header("Understanding Your Menstrual Cycle")
        
        with st.expander("Menstrual Phase (Day 1-5)", expanded=True):
            st.write("""
            This phase, which typically lasts from day one to day five, is the time when the lining of your uterus sheds.
            Most people bleed for three to five days, but a period lasting only three days to as many as seven days is 
            usually not a cause for worry.
            """)
        
        with st.expander("Follicular Phase (Days 1-13)"):
            st.write("""
            This phase typically takes place from days six to 14. During this time, the level of the hormone estrogen rises,
            which causes the lining of your uterus (the endometrium) to grow and thicken. In addition, another hormone —
            follicle-stimulating hormone (FSH) — causes follicles in your ovaries to grow. During days 10 to 14, one of the
            developing follicles will form a fully mature egg (ovum).
            """)
        
        with st.expander("Ovulation Phase (Day 14)"):
            st.write("""
            This phase occurs roughly at about day 14 in a 28-day menstrual cycle. A sudden increase in another hormone —
            luteinizing hormone (LH) — causes your ovary to release its egg. This event is ovulation.
            """)
        
        with st.expander("Luteal Phase (Day 15-28)"):
            st.write("""
            This phase lasts from about day 15 to day 28. Your egg leaves your ovary and begins to travel through your
            fallopian tubes to your uterus. The level of the hormone progesterone rises to help prepare your uterine lining
            for pregnancy. If the egg becomes fertilized by sperm and attaches itself to your uterine wall (implantation),
            you become pregnant. If pregnancy doesn't occur, estrogen and progesterone levels drop.
            """)
        
        st.subheader("What is considered an irregular period?")
        st.write("""
        - Periods that occur less than 21 days or more than 35 days apart
        - Not having a period for three months (or 90 days)
        - Menstrual flow that's much heavier or lighter than usual
        - Period bleeding that lasts longer than seven days
        - Periods that are accompanied by severe pain, cramping, nausea, or vomiting
        - Bleeding or spotting that happens between periods
        """)
    
    with tab2:
        st.header("Choosing Your Products")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Menstrual Cups")
            st.write("- Reusable and eco-friendly")
            st.write("- Can be worn for up to 12 hours")
            st.write("- Requires proper sizing and insertion")
            
            st.subheader("Sanitary Napkins")
            st.write("- Easy to use and widely available")
            st.write("- Disposable options create waste")
            st.write("- Good for light to heavy flow")
        
        with col2:
            st.subheader("Tampons")
            st.write("- Discreet and comfortable")
            st.write("- Need to be changed every 4-8 hours")
            st.write("- Risk of Toxic Shock Syndrome if left too long")
        
        st.write("""
        According to Harvard Health, more than 3000 million women have their periods synchronously at any moment.
        The choice of products depends on various factors:
        - Comfort
        - Environmental impact
        - Ease of use
        """)
    
    with tab3:
        st.header("Menstrual Cycle Tracker")
        
        with st.form("cycle_tracker"):
            col1, col2 = st.columns(2)
            
            with col1:
                start_date = st.date_input("Start Date of Last Period", datetime.today())
                cycle_length = st.number_input("How long did it last? (in days)", min_value=1, max_value=10, value=5)
            
            with col2:
                usual_cycle = st.number_input("Usual Cycle Length (in days)", min_value=21, max_value=35, value=28)
            
            submitted = st.form_submit_button("Track My Cycle")
        
        if submitted:
            current_date = datetime.today()
            days_passed = (current_date - datetime.combine(start_date, datetime.min.time())).days
            day_in_cycle = days_passed % usual_cycle
            upcoming_start = start_date + timedelta(days=usual_cycle)
            
            # Determine current phase
            if day_in_cycle < 5:
                phase = "Menstruation"
                details = [
                    "You are in your menstrual phase.",
                    "Expect bleeding and discomfort."
                ]
                advice = [
                    "Do: Rest, hydrate, and use pain relief if needed.",
                    "Don't: Overexert yourself or skip self-care."
                ]
                prev_stage = "Luteal Phase"
                next_stage = "Follicular Phase"
            elif day_in_cycle < 15:
                phase = "Follicular Phase"
                details = [
                    "You are in your follicular phase.",
                    "Hormone levels are rising."
                ]
                advice = [
                    "Do: Exercise, eat a balanced diet.",
                    "Don't: Stress and unhealthy habits."
                ]
                prev_stage = "Menstruation"
                next_stage = "Ovulation Phase"
            elif day_in_cycle < 23:
                phase = "Ovulation Phase"
                details = [
                    "You are in your ovulation phase.",
                    "Your fertile window is open."
                ]
                advice = [
                    "Do: Have safe sex if desired.",
                    "Don't: Skip protection if not ready for pregnancy."
                ]
                prev_stage = "Follicular Phase"
                next_stage = "Luteal Phase"
            else:
                phase = "Luteal Phase"
                details = [
                    "You are in your luteal phase.",
                    "Hormone levels remain high."
                ]
                advice = [
                    "Do: Manage PMS symptoms, relax.",
                    "Don't: Overindulge in caffeine or stress."
                ]
                prev_stage = "Ovulation Phase"
                next_stage = "Menstruation"
            
            # Display results
            st.subheader("Your Cycle Details")
            
            cols = st.columns(2)
            with cols[0]:
                st.metric("Current Phase", phase)
                st.write("**Details:**")
                for detail in details:
                    st.write(f"- {detail}")
                
                st.write("**Advice:**")
                for item in advice:
                    st.write(f"- {item}")
            
            with cols[1]:
                st.metric("Next Period Expected", upcoming_start.strftime("%b %d, %Y"))
                
                if current_date.date() > upcoming_start:
                    days_late = (current_date.date() - upcoming_start).days
                    st.warning(f"Your period is {days_late} days late")
                
                st.write("**Phase Transition:**")
                st.write(f"Previous: {prev_stage}")
                st.write(f"Next: {next_stage}")

def gynecologist_page(): 
    st.title("Find Nearby Gynecologists")
    
    # Initialize Google Maps client
    import streamlit as st
import streamlit.components.v1 as components

def gynecologist_page():
    
    # Embed Google Maps directly (client-side)
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        /* Modern search box */
        #location {
          padding: 12px;
          width: 70%;
          border: 1px solid #e63946;
          border-radius: 8px;
          font-size: 16px;
          margin-right: 8px;
        }
        
        /* Attractive search button */
        #searchBtn {
          padding: 12px 24px;
          background-color: #e63946;
          color: white;
          border: none;
          border-radius: 8px;
          cursor: pointer;
          font-size: 16px;
          font-weight: 500;
          transition: background-color 0.3s;
        }
        
        #searchBtn:hover {
          background-color: #c1121f;
        }
        
        /* Doctor cards styling */
        .doctor-card {
          background: white;
          border-radius: 10px;
          box-shadow: 0 2px 10px rgba(0,0,0,0.1);
          padding: 16px;
          margin: 12px 0;
          border-left: 4px solid #e63946;
        }
        
        .doctor-card h3 {
          color: #1d3557;
          margin-top: 0;
        }
        
        .details-btn {
          background: #457b9d;
          color: white;
          border: none;
          padding: 8px 16px;
          border-radius: 6px;
          cursor: pointer;
          margin-top: 8px;
        }
        
        /* Scrollable results */
        #results {
          max-height: 500px;
          overflow-y: auto;
          padding-right: 8px;
        }
        
        /* Map container */
        #map {
          height: 300px;
          margin: 16px 0;
          border-radius: 8px;
        }
      </style>
    </head>
    <body>
      <input id="location" type="text" placeholder="Enter your location (city or address)">
      <button id="searchBtn" onclick="findDoctors()">Search Doctors</button>
      
      <div id="map"></div>
      <div id="results"></div>

      <script>
        let map;
        let service;
        const resultsDiv = document.getElementById('results');
        
        function initMap() {
          map = new google.maps.Map(document.getElementById('map'), {
            center: { lat: 20.5937, lng: 78.9629 }, // Default to India
            zoom: 5
          });
          service = new google.maps.places.PlacesService(map);
        }
        
        function findDoctors() {
          const location = document.getElementById('location').value;
          if (!location) return alert("Please enter a location");
          
          resultsDiv.innerHTML = "<p style='text-align:center;'>Searching for gynecologists near you...</p>";
          
          new google.maps.Geocoder().geocode(
            { address: location },
            (results, status) => {
              if (status !== 'OK') return resultsDiv.innerHTML = "<p>Location not found. Please try again.</p>";
              
              const latLng = results[0].geometry.location;
              map.setCenter(latLng);
              map.setZoom(14);
              
              service.nearbySearch(
                {
                  location: latLng,
                  radius: 5000, // 5km radius
                  keyword: 'gynecologist',
                  type: 'doctor'
                },
                (places, status) => {
                  if (status !== 'OK') return resultsDiv.innerHTML = "<p>No gynecologists found in this area. Try a different location.</p>";
                  
                  resultsDiv.innerHTML = "";
                  places.forEach(place => {
                    new google.maps.Marker({
                      map,
                      position: place.geometry.location,
                      title: place.name
                    });
                    
                    const card = document.createElement('div');
                    card.className = 'doctor-card';
                    card.innerHTML = `
                      <h3>${place.name}</h3>
                      <p>📍 ${place.vicinity || 'Address not available'}</p>
                      ${place.rating ? `<p>⭐ ${place.rating}/5 (${place.user_ratings_total || '0'} reviews)</p>` : ''}
                      <button class="details-btn" onclick="getDetails('${place.place_id}', this)">View Details</button>
                      <div id="details-${place.place_id}" style="margin-top:8px;"></div>
                    `;
                    resultsDiv.appendChild(card);
                  });
                }
              );
            }
          );
        }
        
        function getDetails(placeId, button) {
          const detailsDiv = document.getElementById(`details-${placeId}`);
          if (detailsDiv.innerHTML) {
            detailsDiv.innerHTML = '';
            button.textContent = 'View Details';
            return;
          }
          
          button.textContent = 'Loading...';
          
          service.getDetails({ placeId }, (place, status) => {
            button.textContent = 'Hide Details';
            if (status !== 'OK') return detailsDiv.innerHTML = "<p>Details unavailable</p>";
            
            detailsDiv.innerHTML = `
              ${place.formatted_phone_number ? `<p>📞 <a href="tel:${place.formatted_phone_number}">${place.formatted_phone_number}</a></p>` : ''}
              ${place.website ? `<p>🌐 <a href="${place.website}" target="_blank">Visit Website</a></p>` : ''}
              ${place.opening_hours ? `
                <p>🕒 ${place.opening_hours.isOpen() ? 'Currently Open' : 'Currently Closed'}</p>
              ` : ''}
            `;
          });
        }
      </script>
      
      <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCQDm-jvpXkwWZjGi0fY6vDqznYIXOcMjs&libraries=places&callback=initMap" async defer></script>
    </body>
    </html>
    """
    
    components.html(html_code, height=800)

def rights_page(): 
    st.title("Legal Rights and Acts in India")
    st.markdown("---")
    
    # Search functionality
    search_query = st.text_input("Search laws by keyword", placeholder="e.g. marriage, women, workplace")
    
    # Expanded laws data with more acts
    laws = [
        {
            "title": "Guardians & Wards Act, 1890",
            "description": "Governs the appointment of guardians for minors, ensuring child welfare in custody matters."
        },
        {
            "title": "Indian Penal Code, 1860 (Section 354)",
            "description": "Punishes assault or criminal force to woman with intent to outrage her modesty (2-5 years imprisonment)."
        },
        {
            "title": "Protection of Women from Domestic Violence Act, 2005",
            "description": "Provides legal protection against domestic violence including physical, emotional, and economic abuse."
        },
        {
            "title": "Dowry Prohibition Act, 1961",
            "description": "Makes giving or taking dowry illegal with punishments for offenders (min. 5 years imprisonment + fine)."
        },
        {
            "title": "Sexual Harassment at Workplace Act, 2013",
            "description": "Mandates Internal Complaints Committees in all organizations with 10+ employees."
        },
        {
            "title": "Maternity Benefit Act, 1961 (Amended 2017)",
            "description": "Provides 26 weeks paid leave for working women, with creche facilities mandatory for 50+ employees."
        },
        {
            "title": "Equal Remuneration Act, 1976",
            "description": "Guarantees equal pay for equal work regardless of gender."
        },
        {
            "title": "Medical Termination of Pregnancy Act, 1971 (Amended 2021)",
            "description": "Allows abortion up to 24 weeks for special categories including rape survivors and minors."
        },
        {
            "title": "POCSO Act, 2012",
            "description": "Protects children from sexual offenses with strict punishments (20 years to life imprisonment)."
        },
        {
            "title": "Hindu Succession Act, 1956 (Amended 2005)",
            "description": "Gives daughters equal rights in ancestral property as sons."
        },
        {
            "title": "Special Marriage Act, 1954",
            "description": "Allows inter-religion marriages with 30-day notice period to allow for objections."
        },
        {
            "title": "Muslim Women (Protection of Rights on Marriage) Act, 2019",
            "description": "Makes instant triple talaq (divorce) illegal with 3 years imprisonment."
        },
        {
            "title": "Indecent Representation of Women Act, 1986",
            "description": "Prohibits indecent representation of women in advertisements/publications."
        },
        {
            "title": "National Commission for Women Act, 1990",
            "description": "Statutory body to review constitutional safeguards for women and recommend remedies."
        },
        {
            "title": "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
            "description": "Bans sex-selective abortions with 3-5 years imprisonment for violations."
        },
        {
            "title": "Prohibition of Child Marriage Act, 2006",
            "description": "Makes child marriage voidable and prescribes punishments for offenders."
        },
        {
            "title": "Legal Services Authorities Act, 1987",
            "description": "Provides free legal aid to women for all cases (not just criminal matters)."
        },
        {
            "title": "Indian Evidence Act (Section 113B)",
            "description": "Presumption of dowry death if woman dies within 7 years of marriage with evidence of harassment."
        },
        {
            "title": "Code of Criminal Procedure (Section 46)",
            "description": "Special provisions for arrest of women (only female officers can arrest after sunset)."
        },
        {
            "title": "Hindu Widows Remarriage Act, 1856",
            "description": "Legalized remarriage of Hindu widows and gave them inheritance rights."
        }
    ]
    
    # Filter laws based on search
    filtered_laws = [law for law in laws 
                    if not search_query or 
                    search_query.lower() in law["title"].lower() or 
                    search_query.lower() in law["description"].lower()]
    
    # Display laws as dropdowns
    st.subheader(f"Found {len(filtered_laws)} relevant laws")
    
    for law in filtered_laws:
        with st.expander(f"📜 {law['title']}", expanded=False):
            st.markdown(f"""
            <div style="
                padding: 16px;
                background-color: #FFF5F7;
                border-radius: 8px;
                border-left: 4px solid #E63946;
                margin: 8px 0;
            ">
                <p style="color: #555; line-height: 1.6;">{law['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Add practical action buttons
            search_url = f"https://www.google.com/search?q={urllib.parse.quote_plus(law['title'] + ' site:gov.in')}"
            st.markdown(
                f"""
                <a href="{search_url}" target="_blank">
                    <button style="
                        background-color: #E63946;
                        color: white;
                        border: none;
                        padding: 8px 16px;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin: 4px 2px;
                        cursor: pointer;
                        border-radius: 8px;
                        width: 100%;
                    ">
                        🔍 Search "{law['title']}" on Google
                    </button>
                </a>
                """,
                unsafe_allow_html=True
            )


    
    # Additional resources
    st.markdown("---")
    st.subheader("Need legal help?")
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        **National Commission for Women Helpline**  
        📞 7827-170-170  
        [Website](https://ncw.nic.in)
        """)
    with col2:
        st.info("""
        **Legal Aid Services**  
        📞 1800-11-0001  
        [NALSA](https://nalsa.gov.in)
        """)


# Sidebar navigation
with st.sidebar:
    st.title("Naari")
    st.title("Navigation")
    selection = st.radio("Go to:", list(PAGES.keys()))

# Main content area
st.title("Naari - Women's Essentials")

# Display the selected page
page_name = PAGES[selection]
if page_name == "about":
    about_page()
elif page_name == "self_defense":
    self_defense_page()
elif page_name == "menstrual":
    menstrual_page()
elif page_name == "gynecologist":
    gynecologist_page()
elif page_name == "rights":
    rights_page()


# Footer
st.markdown("---")
st.caption("© 2024 Naari | All Rights Reserved")