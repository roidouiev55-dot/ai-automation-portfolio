# 02 · Social Content Agent (Human-in-the-loop)

<div dir="rtl">

**הבעיה:** הפקת תוכן שוטף לאינסטגרם דורשת זמן: איתור נושאים, כתיבה, תמונות, עיצוב במיתוג ופרסום.

**הפתרון:** סוכן שעושה את כל העבודה, ומשאיר לאדם רק החלטה אחת: לאשר או לדחות כל פוסט בטלגרם.

**החלק שלי:** בניתי את הסוכן קודם ב-Make והעברתי אותו ל-n8n (self-hosted ב-Docker). כולל הגדרת אפליקציית מפתחים ב-Meta, חיבור כל ה-APIs ובניית שלושת ה-workflows.

</div>

## Architecture

```mermaid
flowchart TB
    subgraph W1[Workflow 1 · Content Generator · scheduled]
        G1[Schedule trigger] --> G2[OpenAI Responses API + web search: find topic, write post]
        G2 --> G3[OpenAI Images API ×2]
        G3 --> G4[HCTI: render branded slides]
        G4 --> G5[Cloudinary]
        G5 --> G6[(Airtable: status = pending)]
        G6 --> G7[Telegram: carousel + approve / reject buttons]
    end

    subgraph W2[Workflow 2 · Approval Handler]
        H1[Telegram getUpdates polling] --> H2[(Airtable: approved / rejected)]
    end

    subgraph W3[Workflow 3 · Publisher · every 15 min]
        P1[(Approved posts)] --> P2[Instagram Graph API: carousel publish]
        P2 --> P3[(status = published)]
    end

    G7 --> H1
    H2 --> P1
```

## Engineering decisions

<div dir="rtl">

- **אישור אנושי לפני פרסום:** שום פוסט לא עולה בלי אישור בטלגרם.
- **מניעת חזרתיות:** לפני יצירת פוסט, הסוכן בודק מול הפוסטים האחרונים ב-Airtable ומדלג על נושא שכבר פורסם.
- **Polling ולא webhook לאישור:** n8n רץ על localhost, כך שטלגרם לא יכול לשלוח אליו webhook מבחוץ. לכן ה-workflow שואל את טלגרם בעצמו אם יש עדכונים חדשים.
- **ניהול הרשאות:** טוקן עמוד קבוע של Meta, אימות בכותרות הבקשה (Header Auth) ואימות בסיסי (Basic Auth) ל-APIs שאין להם חיבור מובנה ב-n8n.
- **התאמה למגבלות:** תמונות שנשלחות לטלגרם עוברות דחיסה דרך Cloudinary, כדי לעמוד במגבלת הגודל של sendMediaGroup.
- **מודלים:** התחלתי עם Gemini ועברתי ל-OpenAI, אחרי שהחיפוש המעוגן (grounding) בטיר החינמי של Gemini לא נתן תוצאות שמישות.

</div>

## Stack

n8n (Docker, self-hosted) · OpenAI Responses API + web_search · OpenAI Images API · HCTI · Cloudinary · Airtable · Telegram Bot API · Instagram Graph API

<div dir="rtl">

הגרסה הקודמת של הסוכן נבנתה ב-Make, בשלושה תרחישים: יצירת תוכן, טיפול באישור ופרסום.

</div>
