# 🖭 My-Mixtape 🖭

![image](https://github.com/Terafora/My-Mixtape/assets/144109245/065f1a4e-1249-42d5-a405-0a59affedec5)

[My Mixtape is live! Come visit here.](https://my-mix-tapes-a7ee13848429.herokuapp.com)

## About

My Mixtape is a website where you can creates a your own mixtape using various links to songs you enjoy from across the web so that you have all your favourite songs and music video in one centralised location which you can share with your friends. Unlike a simple Youtube  or Spotify list you can add certain retro flare which speaks to your own retro sensibilities while still benefitting from the advances of modern technology.

My Mixtape allows users to take their music on the go with it's responsive and fluid design. Not only will My Mixtape work on your desktop, your tablet or your phone to suit your situation, but it will be moldable by users so that their mixtapes and tracklists truly reflect their unique taste in music. Not only this but each mixtape comes with the ability to add a description to it, so if you're ever looking for a way to share how you feel with someone else, or simply give someone a little note with the music you've compiled for them then you can do just that and add that at the very top before hitting the share button and sharing your mixtape with anyone across the globe.

It is my belief that since the invention of the personal MP3 player that music has become less a communal art and something enjoyed purely in isolation, and I believe it is time to change that which is why My Mixtape aims to bring the social aspect back to soundtracks and once again begin to bring us back together much like the early vision of the internet. If you share this vision then I implore you to come along for the ride and begin making your own mixtapes.

This project uses HTML, CSS, JavaScript for font-end operations, and Django for the backend. As a personal challenge I've also made sure to create all the art assets used by the sites myself using a combination of Figma, and LottieLabs. The site featurea an account system when users can log into a private account so that they can keep their mixtapes private and uneditable friom other users.

![screen-recording_V2](https://github.com/Terafora/My-Mixtape/assets/144109245/7ddab116-bdb2-4cdf-8df9-d902ad09ff4f)

For the project-board associated with this associated with this project, please click [here](https://github.com/users/Terafora/projects/6)

## 💻 Technologies 💻

- HTML
- CSS / Bootstrap 5
- JavaScript
- Python / Django
- Figma + Lottie Labs

## 🎨 Design 🎨
### Figma Design Boards (UX/UI)

The design for My Mixtape ended up being something inspired heavily by 80's synthwave aesthetics, however it was not always envisioned to be this way.
On my first designs and vision for this site the original idea for the presentation was actually a lot more inspired by early 2010's "Hipster" culture.  In particular my inspiration was the HUD elements which were present in Life Is Strange which was released in the same time frame.

Examples:

- [Life Is Strange HUD Example Images 1](https://www.artstation.com/artwork/g2QBYK)
- [Life Is Strange HUD Example Images 2](https://www.gameuidatabase.com/gameData.php?id=672)

When I began to make this however I saw that there was a limited appeal to this design as we aren't far away enough from the early 2010's for this to be nostalgic, while also not close enough to this time period for there to be a broad appeal. It's at this point that I decided to change gears and change up the design with what you see in the live product. The asymetrical, curvy designs were instead made into sleak straight neon lit lines. Unlike the culture of the early 2010's nostalgia for the 80's has been a hot commodity for a seeimgly long time now and with the idea of the site revolving around mixtapes the synthesis of the two was a no brainer, and so you have what you see today.

![Cassette Tape Icons](https://github.com/Terafora/My-Mixtape/assets/144109245/10da6610-38cb-4439-a282-d3e0077ebf6e)

There was more designed than what made it to what is currently the final product and you may be curious about what those other assets may be so I'm providing a link to my Figma design boards below to that you can take a look yourself at what could have been, how my site was envisioned, and some hints at what may be coming in the future.
(Please note this does not contain information or assets about the site prior to changing the theming an 80's synthwave aesthetic).

- [The Figma board for My Mixtape](https://www.figma.com/file/MMXSySr5JDLlYniad0eXKp/My-Mix-Tapes?type=design&node-id=0-1&mode=design) 

### Wireframes

As low-fidelity wireframes were created for each page for mobile, tablet and desktop I will incluge a link to these designs in particular [here.](https://www.figma.com/file/MMXSySr5JDLlYniad0eXKp/My-Mix-Tapes?type=design&node-id=0-1&mode=design).

Higher Fidelity versions of these were also in the process of being created, however were left incomplete due to time restraints.

### Fonts and Colours

The main font for Titles and such was Hurricane. The reason being that it hit the exact style of what has been popular in synthwave and vapourwave communities for a long time now which are both heavily inspired by 80's Americana.

My main colour swatch was the below as the neon blue and pink really drove home the feeling of an idealised version of what the 80s are often thought to be. The decision to go with purple for many buttons and the animated background was to act as a happy medium between the two which wasn't overpowering and distracting for users. Finally black was chosen over white for the main hue as it helped accentuate the bright neon colours while also helping to temper them and cause less strain on the users eyes. 

The decision to remove the animated background for mobile and tablet users was twofold.

- If someone is on a mobile phone the animated backgrounds would take up bandwidth and data neither of which is ideal for the user.
- Using a mobile device in public can be dangerous enough as it takes attention away from a users surroundings. Removing extra distractions in these situtations is only beneficial for users in these situations as helps protect them while using the product.

## Features

My Mixtape allows users to:

- Create, Read, Edit and Delete mixtapes.
- Create, Read, Edit and Delete Tracks on mixtapes.
- Share mixtapes with friends via links to specific tapes.
- Consolidate all the links to users' favourite songs in one stylish package.

### Homepage 🏠

The homepage gives users a little glimpse at the site and gives the general idea of what My Mixtape is all about.

![Screen Recording - Dec 7, 2023](https://github.com/Terafora/My-Mixtape/assets/144109245/41308c99-2dc5-46ab-b87a-1898b0508cef)

### About ❓

The about page goes a little in depth with what My Mixtape is all about, the problem it is solving and a little information about the creator of the website.

![Screen Recording - Dec 7, 2023 (1)](https://github.com/Terafora/My-Mixtape/assets/144109245/7b031e2c-5462-4b5e-9a51-f1c6b521550a)

### Library 📖

The library page is where the magic begins to happen. From here users can create their own mixtapes and what mixtapes they've already created and have stored.

![Screen Recording - Dec 7, 2023 (2)](https://github.com/Terafora/My-Mixtape/assets/144109245/1adc1679-4fbb-41e4-9883-8c386be6065e)

### Mixtapes 🖭

Inside each created mixtape is the view for users to create edit and delete tracks for their mixtapes as well as update the associated information for the mixtape.
In here users are able to go through the tracks they have added and enjoy what they have collected on their personalised mixtape as well as add, delete and edit the tracks on the associated mixtape.
At the top of the page is a share mixtape button which saves the url to the mixtape to the user's clipboard so they can share their mixes with friends and at the bottom of the page is an edit mixtape info button.

![Screen Recording - Dec 7, 2023 (3)](https://github.com/Terafora/My-Mixtape/assets/144109245/92b67f82-764f-47c8-8b58-ae6be8c2be95)

### Login/Logout/Signup 🔒

Nothing could be personalised though without the use of accounts and My Mixtape brings the ability for users to sign up with the website so that they can get to work making mixtapes.
They're also able to login and logout from the site so not only can they gain access to their mixtapes wherever they are but they can also keep their accounts secure with logging out.
A further benefit to this functionality is that it means users can create, edit and delete their own mixtapes and tracks, but are not able to do the same to other user's objects.

### Share! 📨

As I've said before, sharing is one of the most important things we can do with music and it's the main vision of My Mixtape.
At the bottom of every mixtape's tracklist is a little share button that you can click to get your mixtapes link and then you can send it to all of your friends and family no matter where they are in the world. And there's no need to fear, even if someone unscrupulous gets ahold of your mixtape you can rest easy knowing that the security features built in will prevent them from tampering with your mixtapes.

### Unimplemented Features

- Django messages for when certain actions are carried out by the user would be the next thing I would include.
- Further tweeks to styling. Although it looks perfectly presentable and performs to a high standard I personally would like to go back in at a later date to tighten some aspects up as well as work on the overall design recieved from users. In particular the sizing and proportions on 4K monitors which although looks the same as a regular desktop has the effect of icons being too big.
- Due to time restraints I didn't work on it and left it out of scope, however I would very much like to try creating functionality where the linked music plays in the app rather than redirecting users to the source of the music.

## Testing 🧪

All Testing can be found in my seperate TEST.md [here](https://github.com/Terafora/My-Mixtape/blob/main/TEST.md).
  
## Deployment 🚀

- My Mixtape's front-end was deployed to [Heroku](https://www.heroku.com)
  - Using a procfile and requirements.txt Heroku was able to successfully deploy the site
  - The appropriate env variables were setup to allow the app to run as expected.
  - Django settings were setup and further refined throughout the progress of this project to ensure the smooth running and transition of the site as it went from running on a local server to displaying on live.
  - Language options for the site so it could be used more widely.
  - Ability to arrange tracks and mixtapes better.

- My Mixtape's backend was hosted by [ElephantSQL](https://www.elephantsql.com).
  - The backend is a PostgreSQL database.

- This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.
  - Animations/MP4 video files are delivered by Cloudinary.
  - User uploaded images are handled by Cloudinary.

### The live site for My Mixtape can be found right [here](https://my-mix-tapes-a7ee13848429.herokuapp.com).

## An Agile Approach

### [Project Board](https://github.com/users/Terafora/projects/6/views/1)

### A One Person Team

For this project an Agile approach was taken when working throughout its course, and the appropriate kanban/project board can be found above as it not only includes each of the tasks I worked on but uses user stories as the benchmark and criteria I worked towards. These user stories can also be seen in my TEST.md [here](https://github.com/Terafora/My-Mixtape/blob/main/TEST.md) where I show tests against my user stories showing the integrated features.

The approach of setting up user storied into a project board and then working from there was extremely useful as it gave clear view of the horizon I was heading towards, and as a result kept me from getting stuck when I encountered issues when building the site. It also acted as a good compass in that it kept me from getting too distracted with "nice to haves" which weren't required for the MVP of the site. In the end this approach served me much better than a traditional waterfall approach as it allowed me to dynamically change what I was working on within the project which lowered the amount of time lost overall while also being able to actively show that I was contributing to the final release of the site.

### Time Management

The time alloted for making My Mixtape was quite strict and required a lot of focus if I was ever going to get the amount I wanted done to happen. Fortunately with some early starts, late nights and a penchant for action I was able to work my way to creating a site I could happily display to the world.

Much of the project can be cut into two categories; the functionality and the design work.
For creating the MVP of the site the work leaned a lot more heavily towards the functionality of the site as at the end of the day I wanted to at least have something that performed the intended actions should something happen preventing me from getting a fully realised version out.
Once the MVP was done I continued refining it and fixing any bugs/odd behaviour throughout the day while spending the evenings working on the design elements of the site such as layout, SVG images, and animations though this wasn't a strict seperation of time.

The final stretch of the project came down to testing and polishing the application as well as documenting the project, its features and how it came to be.

## Credits

### Content 📰

- With exception to the user uploaded album covers (as can be seen in some screenshots), all the images and animations on this site were created myself (Charlotte Stone) using [Figma](https://www.figma.com/login) and [LottieLabs](https://www.lottielab.com/). 
- Same as above you can view my Figma board to see the assets I created [here](https://shorturl.at/hmqzT) so please enjoy.
- On the above Figma board you will also see some of the images and photographs which I took inspiration from aptly titled "inspiration board".

- This Django project was made after three courses so invariably borrows from them in one way or another these being:
  - [Code Institute](https://codeinstitute.net)
  - [Zero to Mastery](https://zerotomastery.io)
  - [Dee Mc's Learn Django Course](https://www.youtube.com/playlist?list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy)

- [ChatGPT](https://chat.openai.com) was used for minor debugging and content script writing on the site.

- [W3S](https://www.w3schools.com/howto/howto_css_custom_scrollbar.asp) was referenced, in particular for how to style a scroll bar.

- I used [Tim's Markdown Builder](https://tim.2bn.dev/markdown-builder/) to create a template to work from to build the TEST.md

### Images 🖼️

| | | | |
| --- | --- | --- | --- |
| ![Screenshot 2023-12-06 152008](https://github.com/Terafora/My-Mixtape/assets/144109245/c2f83dec-b15a-4f6f-8fc7-f4a4448a066d) | ![Screenshot 2023-12-06 152636](https://github.com/Terafora/My-Mixtape/assets/144109245/7417255e-df87-4cb6-9710-84fb1f6d9f52) |![Screenshot 2023-12-06 153402](https://github.com/Terafora/My-Mixtape/assets/144109245/f4424c7e-d8aa-4c8f-a10c-6e59ab099c87) | ![Screenshot 2023-12-06 153232](https://github.com/Terafora/My-Mixtape/assets/144109245/6375f3ca-a44b-4c72-9677-02b479111eb7)|
| ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/77834f74-fd9e-4d25-a2c8-6713c7454477) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/03d2d71d-b966-46d1-a50c-5edb7dc71929) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/0bf1eec9-59b3-4765-b799-5835ee71e37f) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/6d3a8725-da14-4a7a-9ba7-8a27c79eb68b) |

More images of the site on various pages and devices can be viewed on my [TEST.md](https://github.com/Terafora/My-Mixtape/blob/main/TEST.md)

## Where to find more of my work 👇

- [My Github](https://github.com/Terafora)
- [My Portfolio](https://terafora.github.io/Portfolio-Site/)
- [My LinkedIn](https://www.linkedin.com/in/kimochi-cool/)
