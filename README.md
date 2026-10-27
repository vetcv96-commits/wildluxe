# WildLuxe — National Parks RV Atlas (installable app)

Folder `www/` is the complete app (works offline after first load).

## A) Install as a web app (fastest, no store)
1. Upload the `www/` folder to any HTTPS host (Netlify Drop, Vercel, Cloudflare Pages, GitHub Pages).
2. **Android:** open the URL in Chrome > menu > *Install app*.
3. **iPhone/iPad:** open the URL in Safari > Share > *Add to Home Screen*.

## B) Real Android APK / AAB
Option 1 (no coding): go to pwabuilder.com, paste your hosted URL, choose Android, download the package (APK for testing, AAB for Play Store).
Option 2 (Capacitor, needs Node + Android Studio):
    npm install
    npx cap add android
    npx cap sync android
    npx cap open android      # Android Studio > Build > Build APK(s)

## C) Native iOS app (needs a Mac, Xcode, Apple Developer account)
    npm install
    npx cap add ios
    npx cap sync ios
    npx cap open ios          # Xcode > Product > Archive

## D) Monthly search volumes in the app
No keyword-volume data is bundled (none could be verified). To show real numbers:
1. Export monthly volumes per park from Google Keyword Planner, Semrush, Ahrefs or DataForSEO.
2. Fill `volumes-template.csv` (park rows x Jan..Dec).
3. Run `python csv_to_json.py volumes-template.csv` — this writes `www/volumes.json`.
4. Redeploy. Each park's detail view then shows a "Monthly searches" chart.
