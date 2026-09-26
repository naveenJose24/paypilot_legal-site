# PayPilot legal site

Static, dependency-free pages for GitHub Pages or Cloudflare Pages.

## Before publishing

The current draft uses AppGenie, India, a minimum age of 10, an effective date of 1 September 2026, and a last-updated date of 26 September 2026. Support and privacy contact links use `appgenieteam@gmail.com`.

Have the privacy policy, terms, deletion/retention wording, age language, and jurisdiction reviewed by qualified counsel for every launch market. Confirm live app permissions and third-party providers immediately before publishing.

## Preview locally

From this folder, run `python3 -m http.server 8000`, then open `http://127.0.0.1:8000/`.

## GitHub Pages

Put this folder in the repository you want to publish, enable Pages for the branch and folder containing `index.html`, then add the custom domain in the repository Pages settings and configure the generated DNS records.

## Cloudflare Pages

Create a Pages project from the Git repository. Use `legal-site` as the build output directory if it is inside a larger repository. For this dependency-free site, use an empty build command or `exit 0`, then add the custom domain in Cloudflare Pages.

## Content notes

The pages are grounded in the verified PayPilot behavior: email/Google/Apple sign-in, local-first storage, encrypted Firestore sync, local notifications, Siri/Shortcuts handoff, and in-app account deletion.
