# Testing

Return back to the [README.md](https://github.com/Terafora/My-Mixtape#readme) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com) | ![Home - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/c787ee3c-5697-4d4c-9996-4416da0e4f30) | Pass |
| About | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2Fabout%2F) | ![About - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/f597139a-330b-4708-b393-328421fdcd99) | Pass |
| Library | n/a | ![Library - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/be2212fd-1719-46e8-a298-04cbeeb3ce46) | anchor element inside btn element warning fixed |
| Track_List | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2Fmixtape%2F8%2F) | ![Track List - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/53d42343-6400-4f99-942d-3ce1168b3c40) | anchor element inside btn element warning fixed |
| Add_Track | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2F8%2Fadd_track%2F) | ![Add Track - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/6dc71c93-725d-47cb-98a3-9c7e5af97a28) | Pass. Trailing slash info |
| Update_Track | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2Ftrack%2F8%2Fupdate%2F) | ![Update Track - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/08397646-cf7d-4c86-85b2-d295e75d2ed7) | Pass |
| Track_Confirm_Delete | |![Delete Track - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/f785354b-0368-4a55-9309-1e8792c15751) | Pass. Trailing slash info |
| Add_Mixtape | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2Fadd_mixtape%2F) | ![Add Mixtape - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/08bc79d1-4364-436d-a4cc-f0c69e575442) | Pass. Trailing comma info |
| Edit_Mixtape | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2Fmixtape%2Fedit%2F8%2F) | ![Edit Mixtape - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/255bf4c9-4544-4164-9c65-a0ea01b1520e) | Pass. Trailing slash info |
| Mixtape_Confirm_Delete | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2Fmixtape%2Fdelete%2F5%2F) | ![Delete Mixtape - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/a1102bb5-a9fc-4e5b-b1d9-1b01c2abbe34) | Pass. Trailing slash info |
| Logout | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2Faccounts%2Flogout%2F) |![Logout - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/58fe05f4-d655-430c-80dc-5ebacbe14369) | Pass |
| Login | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2Faccounts%2Flogin%2F) | ![Login - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/493f0769-d177-4120-889a-cf5bce0d2afb) | Pass |
| Signup | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2Faccounts%2Fsignup%2F) | ![Signup - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/17a2afe8-a4f7-43a7-a1f7-d021b386d9c6) | Pass |
| Password_Reset | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2Faccounts%2Fpassword%2Freset%2F) | ![Password Reset - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/902b2509-bd78-4e27-a457-f0eb27bb4291)| Pass |
| 403 | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com%2Ftrack%2F8%2Fupdate%2F) | ![403 - Test](https://github.com/Terafora/My-Mixtape/assets/144109245/4a85642e-76f6-4afc-b638-3ee7b6382825) | Pass. Forced a 403 by trying to edit a track with a different user account to the creator so results show via Edit Track page. |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css & bootstrap from live | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmy-mix-tapes-a7ee13848429.herokuapp.com&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css) |![Screenshot 2023-12-06 120514](https://github.com/Terafora/My-Mixtape/assets/144109245/38cb3b22-ccaf-47e2-9dba-6327f5cf530d) | 16 Errors pointing to css brought in through Bootstrap's stylesheet, 442 warnings in regards to Bootstrap Styles linked in and validator not able to check CSS variables |
| style.css (stand alone)| n/a | ![only css](https://github.com/Terafora/My-Mixtape/assets/144109245/cecfc198-2832-43ab-8ea2-aff4fbc717e5) | Pass |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| share.js & disable.js | ![JS Validation](https://github.com/Terafora/My-Mixtape/assets/144109245/e947c670-cf9c-4736-9164-882c4f85ed54) | Added missing semi-colons that were missing |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | PEP8CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Manage.py | [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Terafora/My-Mixtape/main/manage.py) | ![Screenshot 2023-12-06 143338](https://github.com/Terafora/My-Mixtape/assets/144109245/f17cda93-16ea-4f9d-b864-b0848ad5275c) | Pass |
| Settings.py | [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Terafora/My-Mixtape/main/config/settings.py#) | ![Screenshot 2023-12-06 144038](https://github.com/Terafora/My-Mixtape/assets/144109245/833d5abb-6e2b-4a60-a16b-55cfee630718) | Pass. Updated settings to fix a few overly long lines of code. |
| Config.Urls.py | [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Terafora/My-Mixtape/main/config/urls.py) | ![Screenshot 2023-12-06 144544](https://github.com/Terafora/My-Mixtape/assets/144109245/0ebd22ad-b681-43e9-91a4-ff3f6ff734c9) | Pass |
| Admin.py | [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Terafora/My-Mixtape/main/my_mixtape/admin.py) | ![Screenshot 2023-12-06 145140](https://github.com/Terafora/My-Mixtape/assets/144109245/8b5cb704-37a9-430f-ac7f-e110dd57637e) | Pass. Cleared up white space. |
| Forms.py | [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Terafora/My-Mixtape/main/my_mixtape/forms.py) | ![Screenshot 2023-12-06 145414](https://github.com/Terafora/My-Mixtape/assets/144109245/405d58a1-911a-4990-ad36-91b0d49bed98) | Pass. Cleared up white space. |
| Models.py | [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Terafora/My-Mixtape/main/my_mixtape/models.py) | ![Screenshot 2023-12-06 150238](https://github.com/Terafora/My-Mixtape/assets/144109245/800d9bfe-8199-4c1a-844a-08e278b6e608) | Pass. Cleared up white space issues. |
| My_Mixtape.Urls.py | [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Terafora/My-Mixtape/main/my_mixtape/urls.py) | ![Screenshot 2023-12-06 151008](https://github.com/Terafora/My-Mixtape/assets/144109245/e3d20ad5-5036-40ee-921f-90954d7db6e4) | Pass. Added appropriate fix to overly long lines of code. |
| Views.py | [PEP8CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Terafora/My-Mixtape/main/my_mixtape/views.py)| ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/110a4396-b04f-4ac2-97b3-65d24ae97f96) | Pass with adding appropritate fix to overly long lines and white space. |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/0b33327c-501d-4552-bde0-87fc68b4c26b) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/e082df90-774a-4c85-85b1-c4f3a8c81331) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/bee81c34-2cad-49c8-b867-ea751f246bdf) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/9e3e93f4-5133-4d25-bd6a-19b52cd46e01) | Works as expected |
| Firefox | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/9ab90adc-8e67-43cb-9eea-09d54ef1b04b) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/48822129-81f6-439c-86e6-a37e30ada51b) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/32eaf790-766a-45dd-b2f3-8973cddb4189) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/2883be76-4798-4c22-872f-0d26e35f8c5b) | Works as expected |
| Edge | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/0378a855-c5f5-4127-9223-f79ff9cff9bf) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/294c17a9-3953-4ca8-aa21-7ea4615ad300) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/3d749264-e2f8-4074-991b-4a0b7c4975ba) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/4d48a3a6-f2a1-4b62-95d7-09ce1625ae4e) | Works as expected |
| Opera | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/dd820dde-1cc4-40e0-a335-a73100b88654) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/278d1ffb-e78e-4dcd-af1c-d2fd30954a99) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/5d57e984-c008-4644-bc1b-2f1a83c4e047) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/ac4b5905-ca8f-4953-9037-4b618a799d07) | Works as expected.

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Galaxy Fold (DevTools) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/f396414d-e276-4577-bf93-d093130f65a2) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/448d85e0-a2b8-4560-a49a-e5f50ffc9e82) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/f21441c9-6193-4c59-a099-70aaf7ee09da) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/45b3cd9b-4590-4e0d-a53d-5d23997f2802) | Works as expected |
| iPad Mini (DevTools) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/cc963d9a-1c25-4316-a9ae-773810379cb4) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/3415e057-9f51-48f8-9684-33c55dc9ac55) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/b9f40a81-e945-4903-bd91-bd4b004653d6) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/718d2375-a369-454c-b225-690def41c73c) | Works as expected |
| Desktop | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/626ed329-f03f-4484-875d-4b9e87e446cc)  | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/16714693-356f-43b9-a150-a6cc554fbea0) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/3053330b-4dda-4143-a664-6d807192e2c5) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/d20ff25c-4738-4c47-9ad2-f05762c92afd) | Works as expected |
| Desktop (Portrait) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/70b0211a-5dac-48c6-aa44-01b10908c014) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/186e0289-61af-4621-985b-fad8a58e1ac4) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/22ff59f3-a394-49f2-a91f-07ce22401570) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/bcda9361-c116-4324-9b7e-e304556b634b) | Some minor issues with excessive space towards bottom of page. |
| MS Surface Duo (Single Screen Portrait) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/2e3649d7-e562-4e12-b3ed-af366725269f) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/6a173114-d63c-4447-aa1a-90ebd2f3cff5) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/7719a959-4448-4c2c-b14f-ac40e5b4c2ee) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/a4e71ceb-1604-4272-9be9-74ec273f7300) | Works as expected though edit buttons change colour. |
| MS Surface Duo (Dual-Screen Landscape) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/d31f19a7-3b03-42e8-8bbe-246451627d2c) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/12185235-c66e-4629-beec-faa473388e69) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/640e28f5-2248-44a7-b74b-4b8c07ea23b8) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/6b5fd416-1758-44a9-aec2-f6bb68e74615) | Works as expected though edit buttons siaplay a different colour than expected. |
| Galaxy Tab A | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/46c620f6-9e57-4f48-b0f5-9b8943154af0) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/aee70a18-65da-40e5-a994-6ba7dc531cd0) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/5f7fc45d-6d14-446f-8589-9c411e86101e) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/e5dd7b49-8386-4a2f-8fec-d547503c0e5c) | Works as expected |
| Huawei P30 Pro | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/b9144068-f9a5-465a-8a05-6774cb4dd15d) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/f2b0b954-aa61-4c8e-9ebc-2e390296dcf0) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/786db5ee-f1d8-431a-b7a3-96d9940a9701) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/399c01c3-4c07-4f95-be0c-870ab94994fd) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home |  ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/f28285a3-85cd-47b4-8a05-7d85f7d96e32) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/5412c493-fdc7-44c0-8b81-e8e32e66232f) | Some minor warnings for mobile |
| About | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/cdefd5fe-38dd-46f9-836a-303b86cdbfb1) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/3133484c-ed05-42e9-a8ca-d96c251fc849) | Some minor warnings for mobile |
| Library | n/a | n/a | Lighthouse can't run on this page due to permission issues |
| Tracklist | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/309b6890-6ecb-4ad8-9255-27181863d822) | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/2e66903b-d1f1-4f79-b290-d6c0963aed2f) | Slightly slow response time on mobile due to number of images loading from cloudinary for mobile |

Unable to test edit mixtape, delete mixtape, edit track, delete track due to login being required.

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Sign Up | | | | | |
| | When creating an account the user is expected to fill in all fields. | Tested the feature by trying to submit the form with a variety of incomplete forms.  | The feature behaved as expected, prevented the creation of a user while clarifying the reason. | Test concluded and passed. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/4c6878b1-265a-4c4b-a0e5-454752faafec) |
| | When creating an account the user is expected to provide an adequately strong password. | Tested the feature by using a weak password that doesn't meet the laid out expectations on the page | The account creation was blocked and displayed the appropriate message on screen. | Test concluded and passed. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/0b22167b-e14f-49c9-acda-439d79ac23c2) |
| | When creating an account the user is expected to provide a username not already in use. | Tested the feature by trying to make an account with a username which is already taken. | The feature behaved as expected and showed the appropriate message. | Test concluded and passed. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/07476f21-3223-4138-9b10-df190eeb4de2) |
| | When creating an account the user is expected to provide an email not already in use. | Tested the feature by attempting to make an account with an email which has already in use. | The feature did not respond to A, B, or C. | I did Z to the code because something was missing. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/dfa280c7-2f81-4912-a8d6-20b6ff57f9fb) |
| Login | | | | | |
| | When logging in the user is expected to fill in the full form. | Tested the feature by not filling in every form. | The feature behaved as expected, and prevented login. | Test concluded and passed | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/1343db06-ad0d-498f-8d3a-8276c85dab4e) |
| | When logging in the user needs to provide a correct username to login | Tested the feature by entering an incorrect username/email and password | The feature behaved as expected and prevented user login while providing the reason why login failed. | Test concluded and passed. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/ab15a903-9fee-4078-bcac-4cac34ebf25b) |
| | When logging in the user needs to provide a correct password to login | Tested the feature by entering an incorrect password with correct username | The feature behaved as expected and prevented user login while providing the reason why login failed. | Test concluded and passed. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/c6d22150-2f1b-42cb-b660-c04b4892308b) |
| Add Mixtape | | | | | |
| | When adding a mixtape the user needs to enter a name for the mixtape. | Tested the feature by not entering a name for the mixtape. | The feature behaved as expected, and it prevented the creation of the mixtape while providing the adequate message. | Test concluded and passed. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/a9f07918-9902-48d0-a545-d801f2f46f5c) |
| | When adding a mixtape the user shouldn't be able to add more than one at a time. | Tested the feature by hitting the button multiple times to try and replicate making multiple mixtapes. | Test concluded and passed. | Was previously fixed by disabling the create button after first click. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/bb30e295-e8bc-4b8d-9780-e608a44c1cb5) |
| Add Track | | | | | |
| | When adding a track the user needs to enter a title for it to be accepted. | Tested the feature by not typing in the title field. | The feature behaved as expected, prevented creation while providing the appropriate message to the user. | Test concluded and passed. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/53174283-dd69-4f60-a49c-a36fa91a9095)) |
| | When adding a track the user shouldn't be able to hit submit multiple times. | Tested the feature by hitting submit button multiple times | The feature behaved as expected and the button became disabled after the first press. | Was previously fixed by disabling the create button after first click. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/50356d7a-2ae7-4d5f-9095-2f7f0711d8b8) |
| | When adding a track the user needs to enter a link for it to be accepted. | Tested the feature by not typing in the link field as well as typing a non link. | The feature behaved as expected, prevented creation while providing the appropriate message to the user. | Test concluded and passed. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/18ffda78-3fd2-4bae-873c-e33c5b53574c) |
| Delete Other User Track | | | | | |
| | When trying to delete a track the user needs to be the creator of the track to delete the object. | Tested the feature by trying to delete a track as a seperate user. | The feature behaved as expected, and sent me to a 403 page. | Test concluded and passed. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/7aa351d1-d218-4843-b9d6-1d2197d920c5) |
| Edit Other User Track | | | | | |
| | When trying to wdit a track the user needs to be the creator of the track to edit the object. | Tested the feature by trying to edit a track as a seperate user. | The feature behaved as expected, and sent me to a 403 page. | Test concluded and passed. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/be5d74af-24ee-4adf-b8e6-9528d9ae6cb5) |
| Delete Other User Mixtape | | | | | |
| | When trying to delete a mixtape the user needs to be the creator of the mixtape to delete the object. | Tested the feature by trying to delete a mixtape as a seperate user. | The feature behaved as expected, and sent me to a 403 page. | Test concluded and passed. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/7aa351d1-d218-4843-b9d6-1d2197d920c5) |
| Edit Other User Mixtape | | | | | |
| | When trying to edit a mixtape the user needs to be the creator of the mixtape to edit the object. | Tested the feature by trying to edit a mixtape as a seperate user. | The feature behaved as expected, and sent me to a 404 page. | Test concluded and passed. In the future I will create a unique 404 page | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/46d2c7ee-9878-491c-94b0-99ed4f903fac) |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a user I can login to a personal account so that my created lists are saved. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/4b6b72fe-0d61-404a-ba0e-7b86ae57bc2a) |
| As a user I can Save songs to a list so that I can access them whenever I want. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/8d10ee4e-1fe0-4d7f-a204-a5b59fea149e) |
| As a user I can share mix tapes with other people so that I can share my music with others. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/253bba6c-fbf0-4f05-af4b-2a9fc168d772) |
| As a user I want to use a website that looks nice as well as achieves a goal so that I enjoy being on the site. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/9eadd5d7-aa10-477b-9f39-8b695fb94ae7)|
| As a user I can delete previously created mixtapes so that I can clear up space in my collection. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/a4c7e619-803f-43c0-aa82-4e8af007ead4) |
| As a user I can edit data in regards to mix tapes so that I can correct/update information relating to them. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/3c6a0463-ac27-46b3-a000-dd2b3047f2ff) |
| As a user I can add tracks to mixtapes so that I can make unique selections of music. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/f85f72b7-045e-4156-a647-6505dd1a532f) |
| As a user I can edit track info in mixtapes so that I can correct information that I may have put in incorrectly or may have changed since I originally entered it. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/895f1129-cb83-435f-9e5b-eba5c5766657) |
| As a potential user I want I can see more about the application and the creator so that I can make an informed decision on whether I want to use this product. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/a54ca26c-f665-4eda-8c6a-367514edaed1) |
| As a user I want to be able to see the images that are a part of the website design as well as user uploaded images so that I can fully enjoy using the site. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/0abb53f1-dfaf-41bb-81f0-4f070bf26b65) |
| As a user I can delete tracks from within individual mix tapes so that I can remove songs I no longer want to listen to or enjoy. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/95c670a2-15fd-4cdc-9ccf-943e53831c2e) |
| As a user I can view animated content throughout the site so that I can further enjoy what would otherwise enjoy what would be a static site. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/78430f6f-d3ff-40da-a23b-13d77f764389) |
| As a user I often like to take my music out with me on my phone and so I need a responsive site layout so that I can easily access my links to music on other sites while on the go. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/b15a3e79-29da-4b9a-adea-d1a5ab69d3e7) |
| As a user I can view mixtapes, their info and their tracks after I create them so that I can enjoy the functionality of my mixtapes. | ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/55448f76-8eb1-430f-a5e9-77b220d3ddb4) |
| As a user I can view the tracks that are in each mixtape so that I can see what tracks are and aren't in each of my mixtapes.| ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/d50e99c3-32bf-4841-a054-95b1a309601f) |

## Bugs

- Users were able to create multiple versions of the same mixtape and track by clicking the create/add buttons mulitple times before the page had reloaded

    ![image](https://github.com/Terafora/My-Mixtape/assets/144109245/c1a0fcd0-d6d0-457f-9324-5aa9e72db143)

    - To fix this, I made a JS function which listened to the add/create buttons on the relevant pages and if the button was pressed once then the button would become disabled on a second press preventing more than a single mixtape/track to be created at one time.

- Generally speaking bugs were dealt with as they arose throughout the project. The above is the only standout quirky issue that occurred and as such had an issue raised around it.

### GitHub **Issues**

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here]([https://github.com/Terafora/My-Mixtape/issues?q=is%3Aissue+is%3Aclosed](https://github.com/Terafora/My-Mixtape/milestone/5?closed=1)).

| Bug | Status |
| --- | --- |
| [Duplicate Mixtape & Track Creation](https://github.com/Terafora/My-Mixtape/issues/21) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/Terafora/My-Mixtape/issues).

#### Currently no open bugs 

## Unfixed Bugs

A layout irregularity was caught on testing where the background container for the track list page stretches further below tracks in the list than expected.

There are no remaining bugs outside of what is mentioned above that I am aware of. If you find any I would be very appreciative if you could let me know.
