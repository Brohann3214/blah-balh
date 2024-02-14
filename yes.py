import time

import scratchattach as scratch3

session = scratch3.Session(".eJxVkMtqwzAURP_F69aVbEmWskubPmjBi1JoshJ6XNuKYynYCoGW_nsl8CbbmeHM3PtbXBaYvZqg2BTvagl-Oytd3BUxjOCT1ulaU0W0BVAEaaOFEUBqLDSjuGJ68_I1fzdIPLXPr8ZwKXdvzce-b_do4glzCr3z9-6cSBiRssK8ZKLEDCdPqkscZO6XzuZAJepGNCJ79qh8H2R0E_wEn8dtJ5idUQ8tXOUhzOMtYFDLkELAqQbEG2Es6xhBrLKGW9oRQWqjkOXE0ppTkQ-EJZoQRpfh1wQEe4vUyqQX5GFZAx9Te3TBl6uxlJ9wPq3i4xr--wfAjWwv:1rZsQG:z_MN2f7p10jHfT8yEOKJI5qrhvk", username="JasonArab") #The username field is case sensitive

user = session.get_linked_user()

while True:
    follower_count = user.follower_count()
    user.set_bio(f"My follower count: {follower_count}")
    time.sleep(60) # The follower count is updated every 60 seconds