/** Run against a separately cloned, explicit Reqwise OSS commit. No Figma writes. */
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const [payloadFile, upstreamDir] = process.argv.slice(2);
if (!payloadFile || !upstreamDir) {
  console.error('Usage: npx tsx tests/integration/check_reqwise_schema.ts payloads.json path-to-reqwise-checkout');
  process.exit(2);
}
const source = pathToFileURL(resolve(upstreamDir, 'src/server/validate.ts')).href;
const validators = await import(source);
const methods: Record<string, string> = {
  activity: 'validateActivitySpec',
  sequence: 'validateSequenceSpec',
  state: 'validateStateSpec',
  erd: 'validateErdSpec',
  userflow: 'validateUserflowSpec',
  sitemap: 'validateSitemapSpec'
};
const payloads = JSON.parse(readFileSync(payloadFile,'utf8'));
let failures=0;
if (!Array.isArray(payloads) || payloads.length !== Object.keys(methods).length) {
  throw new Error('Expected one payload for each of six OSS diagram types');
}
const actual = new Set<string>();
for (const p of payloads) {
  const type = p?.arguments?.type;
  if (actual.has(type) || !methods[type]) {
    throw new Error('Duplicate or unknown diagram type: ' + String(type));
  }
  actual.add(type);
  if (p?.writes_performed !== false || p?.arguments?.spec?.options?.dryRun !== true) {
    throw new Error('Contract test must never request native Figma writes');
  }
  try {
    validators[methods[type]](p.arguments.spec);
    console.log('UPSTREAM_SCHEMA_OK', type);
  } catch (err) {
    failures++;
    console.error('UPSTREAM_SCHEMA_FAIL',type,(err as Error).message);
  }
}
console.log('Reqwise upstream schema:',payloads.length-failures,'/',payloads.length);
if (failures) process.exitCode=1;
