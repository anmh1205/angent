# Provider release and activation evidence

The two source manifests are package identity, not proof of the plugin installed in a ChatGPT, Codex or other host. The unified ANGENT distribution exposes 12 Core + 102 Engineer Skills, while keeping 103 portable Engineer source identities (including `ak-explain`); the separate Engineer fallback should not also be active for the same workflow.

Run source-only check:

    python3 scripts/verify_activation.py

A successful source check deliberately reports PROVIDER_NOT_CHECKED.

After the provider has an installed release, collect a current observation from the provider's plugin metadata and **complete paginated file listing**. Normalize to a local JSON file outside tracked source (never commit plugin identifiers or private provider output):

    {
      "name": "angent",
      "version": "<observed-installed-version>",
      "complete_listing": true,
      "paths": ["skills/angent/SKILL.md", "... all installed paths ..."],
      "other_active_plugins": [],
      "sha256_by_path": {
        "skills/angent/SKILL.md": "...actual installed content SHA256...",
        "skills/angent-authoring/SKILL.md": "...",
        "skills/angent-quality/SKILL.md": "..."
      }
    }

Then:

    python3 scripts/verify_activation.py --observed /path/to/live-provider.json

The helper checks manifest release version, exact discoverable skill set, duplicate active Engineer and three Core source fingerprints. A catalog/version match without content hashes is limited inventory evidence. A three-file content match **still does not attest the full archive or actual cognitive activation**: separately exercise representative skills in a live model/harness and confirm observed tool/output behavior. Source-only CI cannot set the provider receipt or claim deployment success.

A plugin merely present in the user's owned-plugin catalog is not necessarily loaded; populate other_active_plugins only when the host actually exposes or confirms concurrent activation. Do not treat a presumed installation as observed activity.

For release, inspect provider version and actual activation first, then run authoring benchmark comparisons on the loaded candidate and baseline. A source bump alone must never be reported as installed/verified.
