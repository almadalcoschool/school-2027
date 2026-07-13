# Alma Dal Co School - Website Configuration Guide

This website is a Jekyll-based static site hosted on GitHub Pages. It is structured to easily transition from one school edition to the next (e.g., preparing for the 2029 edition) by updating centralized configuration files and data collections.

---

## 1. Project Architecture

### Central Configuration
* **`_config.yml`**: Contains all global site variables. Modifying this file updates the details (dates, locations, registration status, flyer documents, etc.) site-wide.

### Collections (Dynamic Content)
* **`_attendees/`**: Holds markdown files for each invited speaker.
  * *Required fields*: `name`, `position`, `image_path`, `website`, `category`, and `bio`.
* **`_organizers/`**: Holds markdown files for organizers, committees, and webmasters.
  * *Required fields*: `name`, `position`, `role`, `image_path`, and `website`.
  * *Valid roles* (used to categorize them on the Organizers tab):
    * `Chairperson` (or `Chairperson (Co-chair)`)
    * `Scientific Committee`
    * `Local Organizing Committee`
    * `Webmasters`

### Styling & Layouts
* **`_sass/`**: Contains modular SASS stylesheets (`layout.scss`, `navigation.scss`, `staff.scss`, etc.) that compile into the main stylesheet.
* **`_layouts/`**: Contains structural page templates (`default.html`, `home.html`).
* **`css/screen.scss`**: The entry point for the compiled CSS, configured with cache-busting versioning inside `_layouts/default.html`.

### Assets
* **`images/attendees/`**: Circular profile pictures for invited speakers.
* **`images/organizers/`**: Circular profile pictures for organizers and webmasters.
* **`images/pictures_gallery/`**: General banners and event photos.

---

## 2. Running Locally

To run the site locally for testing before pushing changes:

1. Install **Ruby** (v3.0+) and **Bundler**.
2. Run `bundle install` in the root directory to install dependencies (Jekyll, plugins).
3. Start the local server:
   ```bash
   bundle exec jekyll serve
   ```
4. Open `http://127.0.0.1:4000/` in your browser.

---

## 3. Transitioning to a New Edition (e.g. 2029 School)

Follow these steps to update the website for a future edition:

### Step 1: Update Global Variables in `_config.yml`
Open `_config.yml` and update the following fields:
* `event_dates`: Change to the new 2029 dates (e.g., `10th – 16th of September, 2029`).
* `registration_status`: Set to `"Open"`, `"to come"`, or `"Closed"`.
* `flyer_pdf`: Update the filename of the downloadable school poster/flyer.
* `contact_name` / `contact_email` / `contact_phone`: Update if the organizing secretariat changes.

### Step 2: Upload New Flyer and Banners
* Place the new flyer PDF in the root directory and ensure its filename matches the `flyer_pdf` value in `_config.yml`.
* Update page banner images in the frontmatter of individual markdown files (e.g., `index.md`, `alma.md`, `venue.md`) pointing to new pictures in `images/pictures_gallery/`.

### Step 3: Update Speakers
1. **Remove or Archive Old Speakers**:
   * Delete or move the old speaker markdown files from `_attendees/`.
2. **Add New Speakers**:
   * Create a new `.md` file in `_attendees/` for each new speaker (use their last name, e.g. `Ackermann.md`).
   * Example template:
     ```yaml
     ---
     name: Martin Ackermann
     position: ETH, Zurich, CHE
     image_path: /images/attendees/Ackermann.jpg
     website: "https://www.eawag.ch"
     category: "Pattern Formation Across Scales"
     bio: |
       Short biography text goes here...
     ---
     ```
3. **Upload Photos**:
   * Upload their profile pictures to `images/attendees/`.
   * **Important**: Use clean ASCII filenames (e.g., `Juelicher.jpg` instead of `Jülicher.jpg`) to prevent URL rendering bugs on Linux-based web servers.

### Step 4: Update Committees and Organizers
1. **Modify Organizers**:
   * Add, remove, or edit profile markdown files under `_organizers/`.
2. **Upload Photos**:
   * Add their profile pictures to `images/organizers/` and assign them in the profile frontmatter `image_path` key.

### Step 5: Update the Scientific Program Table
* Open **`scientific_program.md`** and update the timetable markdown grid.

### Step 6: Deploy
* Push all updates to the `main` branch of the official repository. GitHub Pages will build and deploy the changes automatically.
