# AI Automation Portfolio — Roi Douiev

<div dir="rtl">

**רועי דוייב | AI Solution Implementer**

סוכני AI, אוטומציות ואינטגרציות שבניתי והפעלתי בפועל. כל פרויקט מתועד לפי מבנה קבוע: הבעיה שהוא פותר, הארכיטקטורה, הכלים וההחלטות הטכניות שקיבלתי.

</div>

| # | Project | Stack | Status |
|---|---------|-------|--------|
| 1 | [BAGALIL Video Agent](projects/01-video-agent/) | Make · Gemini API · Telegram Bot · Cloudinary · HCTI · Airtable | In production |
| 2 | [Social Content Agent (Human-in-the-loop)](projects/02-content-agent/) | n8n · OpenAI API · HCTI · Cloudinary · Airtable · Telegram · Instagram Graph API | Built, rebuilt from Make to n8n |
| 3 | [Multi-Agent System + Telegram Control Hub](projects/03-multi-agent/) | Claude Code · Telegram · curated knowledge bases | Running on a local machine |
| 4 | [Internal Management Dashboard](projects/04-internal-dashboard/) | Next.js · Supabase · Vercel · Gemini API | Internal tool |

<div dir="rtl">

### מה חוזר בכל הפרויקטים

- **ארכיטקטורה מחולקת לשלבים:** כל שלב (יצירה, עיבוד, מסירה) רץ בנפרד, ומסד נתונים משותף מחזיק את הסטטוס של כל רשומה.
- **אמינות:** retry מול שגיאות 429 ו-503, מניעת כפילויות, וענף שגיאה שרושם את התקלה ברשומה עצמה.
- **אדם בתוך הלולאה:** כשצריך, תוכן לא מתפרסם בלי אישור בטלגרם.
- **אבטחה:** אין מפתחות או טוקנים בקוד. ב-repo הזה הוסרו כל המזהים הרגישים.

</div>

## Contact

Roidouiev55@gmail.com
