from pathlib import Path

DOCS = Path(__file__).resolve().parents[1] / 'docs'
LANG_DIR = DOCS / 'lang'
LANG_DIR.mkdir(parents=True, exist_ok=True)

LANGS = {
    'he': {
        'lang': 'he', 'dir': 'rtl', 'label': 'עברית',
        'brand': 'עלית / שטראוס · נוף הגליל',
        'title': 'מערכות אמיתיות. אחריות אמיתית.',
        'lead': 'אנחנו מחפשים הנדסאי/ת אחזקה, טכנאי/ת אנרגיה, ובעלי ניסיון מוכח במדחסי אוויר, צ׳ילרים ודוודים.',
        'section': 'זה לא רק עוד תפקיד טכני',
        'section_p': 'זו עבודה בלב המערכות שמחזיקות ייצור אמיתי: אוויר, חום, קירור, מים ואדים — עם אחריות שאפשר להרגיש בשטח.',
        'boiler_t': 'הלב האנרגטי של המפעל',
        'boiler_p': 'מאחורי כל קו ייצור יש מערכות שלא רואים על המדף — אבל בלעדיהן שום דבר לא זז.',
        'boiler_top': '01 · הלב האנרגטי',
        'comp_top': '02 · חדר מדחסי אוויר',
        'comp_t': 'כאן המפעל נושם',
        'comp_p': 'מדחסי אוויר, צ׳ילרים, דוודים ותשתיות אנרגיה — עבודה טכנית אמיתית בסביבה תעשייתית אמיתית.',
        'fit_t': 'למי זה מתאים?',
        'fit_p': 'מי מתאים, למה לפנות, ומה עושים עכשיו.',
        'cards': [('הנדסאים עם ניסיון','אנשים שכבר מכירים מערכות תעשייתיות, אנרגיה או אחזקה.'), ('בתחילת הדרך?','הנדסאים והנדסאיות שרוצים ללמוד מקצוע אמיתי מהשטח.'), ('ניסיון גם בלי תעודה','אם יש ניסיון רלוונטי במדחסי אוויר, צ׳ילרים או דוודים — בוא/י נדבר.')],
        'cta_t': 'מתאים לך?', 'cta_p': 'כתבו לנו — ונחזור עם פרטים על התפקיד, המשמרות וההתאמה לצוות האנרגיה.', 'cta_b': 'פרטי קשר יתווספו כאן',
        'systems': ['מדחסי אוויר','צ׳ילרים','דוודים','מים ואדים']
    },
    'en': {
        'lang': 'en', 'dir': 'ltr', 'label': 'English',
        'brand': 'Strauss / Elite · Nof HaGalil',
        'title': 'Real systems. Real responsibility.',
        'lead': 'We are looking for maintenance practical engineers, energy technicians, and people with proven experience in air compressors, chillers and boilers.',
        'section': 'This is not just another technical role',
        'section_p': 'This is work at the heart of the systems that keep real production running: air, heat, cooling, water and steam — with responsibility you can feel on the floor.',
        'boiler_t': 'The energy heart of the factory',
        'boiler_p': 'Behind every production line there are systems outsiders rarely see — but without them, nothing moves.',
        'boiler_top': '01 · Energy heart',
        'comp_top': '02 · Air compressor room',
        'comp_t': 'This is where the factory breathes',
        'comp_p': 'Air compressors, chillers, boilers and energy infrastructure — real technical work in a real industrial environment.',
        'fit_t': 'Who is this for?', 'fit_p': 'Who fits, why to reach out, and what to do now.',
        'cards': [('Experienced practical engineers','People who already know industrial systems, energy or maintenance.'), ('Early in your career?','Young practical engineers who want to learn a real trade from the field.'), ('Experience even without a certificate','If you have relevant hands-on experience with air compressors, chillers or boilers — let’s talk.')],
        'cta_t': 'क्या यह आपके लिए है?', 'cta_p': 'Write to us — we will get back to you with details about the role, shifts and fit for the energy team.', 'cta_b': 'Contact details will be added here',
        'systems': ['Air compressors','Chillers','Boilers','Energy']
    },
    'ar': {
        'lang': 'ar', 'dir': 'rtl', 'label': 'العربية',
        'brand': 'Strauss / Elite · نوف هجليل',
        'title': 'أنظمة حقيقية. مسؤولية حقيقية.',
        'lead': 'نبحث عن تقنيي صيانة، تقنيي طاقة، وأشخاص لديهم خبرة مثبتة في ضواغط الهواء، التشيلرات والغلايات.',
        'section': 'هذا ليس مجرد دور تقني آخر',
        'section_p': 'هذا عمل في قلب الأنظمة التي تُبقي الإنتاج الحقيقي يعمل: هواء، حرارة، تبريد، مياه وبخار — مع مسؤولية تُشعر بها في الميدان.',
        'boiler_t': 'القلب الطاقي للمصنع',
        'boiler_p': 'خلف كل خط إنتاج توجد أنظمة لا تُرى من الخارج — لكن من دونها لا يتحرك شيء.',
        'boiler_top': '01 · القلب الطاقي',
        'comp_top': '02 · غرفة ضواغط الهواء',
        'comp_t': 'هنا يتنفس المصنع',
        'comp_p': 'ضواغط هواء، تشيلرات، غلايات وبنية تحتية للطاقة — عمل تقني حقيقي في بيئة صناعية حقيقية.',
        'fit_t': 'لمن هذا مناسب؟', 'fit_p': 'من يناسب، لماذا يتواصل، وما هي الخطوة التالية.',
        'cards': [('تقنيون عمليّون مع خبرة','أشخاص يعرفون مسبقًا أنظمة صناعية، طاقة أو صيانة.'), ('في بداية الطريق؟','تقنيون عمليّون يريدون تعلّم مهنة حقيقية من الميدان.'), ('خبرة حتى بدون شهادة','إذا لديك خبرة عملية مع ضواغط الهواء، التشيلرات أو الغلايات — لنتحدث.')],
        'cta_t': 'هل هذا مناسب لك؟', 'cta_p': 'اكتبوا لنا — وسنعود إليكم مع تفاصيل الوظيفة، الورديات ومدى الملاءمة لفريق الطاقة.', 'cta_b': 'سيتم إضافة تفاصيل التواصل هنا',
        'systems': ['ضواغط هواء','تشيلرات','غلايات','طاقة']
    },
    'ru': {
        'lang': 'ru', 'dir': 'ltr', 'label': 'Русский',
        'brand': 'Strauss / Elite · Ноф-а-Галиль',
        'title': 'Настоящие системы. Настоящая ответственность.',
        'lead': 'Ищем техников, инженеров-практиков и людей с подтверждённым опытом работы с воздушными компрессорами, чиллерами и бойлерами.',
        'section': 'Это не просто ещё одна техническая должность',
        'section_p': 'Это работа в сердце систем, которые держат реальное производство: воздух, тепло, охлаждение, вода и пар — с ответственностью, которую видно на месте.',
        'boiler_t': 'Энергетическое сердце завода',
        'boiler_p': 'За каждой производственной линией стоят системы, которые остаются за кулисами — но без них ничего не работает.',
        'boiler_top': '01 · Энергетическое сердце',
        'comp_top': '02 · Компрессорная',
        'comp_t': 'Здесь завод дышит',
        'comp_p': 'Воздушные компрессоры, чиллеры, бойлеры и энергетическая инфраструктура — настоящая техническая работа в настоящей промышленной среде.',
        'fit_t': 'Кому это подходит?', 'fit_p': 'Кто подходит, зачем писать и что делать дальше.',
        'cards': [('Техники / инженеры-практики с опытом','Люди, которые уже знают промышленные системы, энергию или обслуживание.'), ('В начале пути?','Молодые специалисты, которые хотят учиться настоящей профессии на месте.'), ('Опыт даже без диплома','Если есть реальный опыт с воздушными компрессорами, чиллерами или бойлерами — давайте поговорим.')],
        'cta_t': 'Подходит вам?', 'cta_p': 'Напишите нам — мы вернёмся с деталями по вакансии, сменам и соответствию команде энергии.', 'cta_b': 'Контакт будет добавлен здесь',
        'systems': ['Компрессоры','Чиллеры','Бойлеры','Энергия']
    },
    'hi': {
        'lang': 'hi', 'dir': 'ltr', 'label': 'हिन्दी',
        'brand': 'Strauss / Elite · Nof HaGalil',
        'title': 'असली प्रणालियाँ। असली ज़िम्मेदारी।',
        'lead': 'हम रखरखाव practical engineers, ऊर्जा technicians और air compressors, chillers और boilers में प्रमाणित अनुभव वाले लोगों की तलाश कर रहे हैं।',
        'section': 'यह सिर्फ़ एक और तकनीकी भूमिका नहीं है',
        'section_p': 'यह उन प्रणालियों के केंद्र में काम है जो असली production को चालू रखती हैं: हवा, गर्मी, cooling, पानी और steam — field में महसूस होने वाली ज़िम्मेदारी के साथ।',
        'boiler_t': 'कारख़ाने का ऊर्जा हृदय',
        'boiler_p': 'हर production line के पीछे ऐसी systems होती हैं जो आम लोग नहीं देखते — लेकिन उनके बिना कुछ भी नहीं चलता।',
        'boiler_top': '01 · ऊर्जा हृदय',
        'comp_top': '02 · Air compressor room',
        'comp_t': 'यहीं factory सांस लेती है',
        'comp_p': 'Air compressors, chillers, boilers और energy infrastructure — real industrial environment में real technical work.',
        'fit_t': 'यह किसके लिए है?', 'fit_p': 'कौन fit है, क्यों contact करे, और अगला step क्या है।',
        'cards': [('अनुभवी technicians / practical engineers','जो लोग industrial systems, energy या maintenance पहले से जानते हैं।'), ('करियर की शुरुआत में?','Young practical engineers जो field से real profession सीखना चाहते हैं।'), ('सर्टिफिकेट के बिना भी अनुभव','अगर air compressors, chillers या boilers में relevant hands-on experience है — बात करते हैं।')],
        'cta_t': 'क्या यह आपके लिए है?', 'cta_p': 'हमें लिखें — हम role, shifts और energy team fit की details के साथ वापस संपर्क करेंगे।', 'cta_b': 'Contact details यहाँ जोड़ी जाएँगी',
        'systems': ['Air compressors','Chillers','Boilers','Energy']
    }
}

CSS = r'''
:root{--bg:#07090c;--ink:#fff8ea;--muted:#cfc5af;--gold:#ffb72d;--line:rgba(255,255,255,.14)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#07090c;color:var(--ink);font-family:'Heebo','Noto Sans Arabic','Noto Sans Devanagari',Arial,sans-serif;line-height:1.45;overflow-x:hidden}body:before{content:"";position:fixed;inset:0;pointer-events:none;background:radial-gradient(circle at 70% 0%,rgba(255,183,45,.18),transparent 34%),linear-gradient(#090d12,#07090c);z-index:-2}.wrap{width:min(1120px,100%);margin:auto;padding:20px 14px 54px}.lang-switch{position:sticky;top:8px;z-index:12;display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:0 0 14px;direction:ltr}.lang-switch a{background:rgba(255,255,255,.09);border:1px solid var(--line);color:var(--ink);text-decoration:none;border-radius:999px;padding:8px 11px;font-weight:900;font-size:14px}.lang-switch a.active{background:var(--gold);color:#111}.hero{min-height:70svh;display:grid;align-items:center;position:relative;border-radius:34px;overflow:hidden;border:1px solid var(--line);box-shadow:0 35px 120px rgba(0,0,0,.55);background:#111;margin-bottom:18px}.hero img,.photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:grayscale(.45) contrast(1.06) brightness(.84)}.hero:after,.photo:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.22),rgba(0,0,0,.62)),linear-gradient(90deg,rgba(0,0,0,.12),rgba(0,0,0,.54));z-index:1}.hero-content{position:relative;z-index:2;padding:clamp(22px,5vw,58px);max-width:980px}.eyebrow{color:var(--gold);font-weight:900;font-size:clamp(14px,3vw,18px);margin-bottom:10px}h1{font-size:clamp(40px,9vw,92px);line-height:1.02;margin:0 0 16px;letter-spacing:-.035em;text-wrap:balance}.lead{font-size:clamp(20px,4.6vw,32px);line-height:1.24;color:#f0e7d4;max-width:900px;margin:0}.systems{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}.systems span{background:rgba(255,183,45,.16);border:1px solid rgba(255,183,45,.38);color:#ffe4a3;border-radius:999px;padding:9px 13px;font-weight:900;font-size:clamp(14px,3.4vw,18px)}.section-title{text-align:center;margin:36px auto 16px;max-width:880px}.section-title h2{font-size:clamp(30px,7vw,58px);line-height:1.05;margin:0 0 10px;letter-spacing:-.03em}.section-title p{margin:0;color:var(--muted);font-size:clamp(16px,3.8vw,21px)}.story{display:grid;gap:18px;margin-top:18px}.photo{position:relative;min-height:60svh;border-radius:32px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 100px rgba(0,0,0,.44);background:#111}.photo-content{position:relative;z-index:2;min-height:60svh;display:flex;flex-direction:column;justify-content:space-between;padding:clamp(20px,5vw,54px)}.topline{align-self:flex-start;background:rgba(0,0,0,.46);border:1px solid rgba(255,255,255,.16);backdrop-filter:blur(10px);border-radius:999px;padding:10px 14px;color:#ffe6aa;font-weight:900}.copybox{max-width:820px;background:rgba(5,7,10,.66);border:1px solid rgba(255,255,255,.16);backdrop-filter:blur(14px);border-radius:26px;padding:clamp(18px,4vw,30px);box-shadow:0 18px 70px rgba(0,0,0,.36)}.copybox h3{font-size:clamp(30px,7vw,58px);line-height:1.03;margin:0 0 10px}.copybox p{font-size:clamp(17px,4vw,24px);color:#e8decb;margin:0}.fit{display:grid;grid-template-columns:1fr;gap:14px;margin:22px 0}@media(min-width:780px){.fit{grid-template-columns:repeat(3,1fr)}}.fit-card{background:linear-gradient(180deg,rgba(255,255,255,.075),rgba(255,255,255,.035));border:1px solid var(--line);border-radius:26px;padding:22px;min-height:160px}.fit-card b{display:block;color:var(--gold);font-size:22px;margin-bottom:8px}.fit-card p{margin:0;color:var(--muted);font-size:17px}.cta{margin-top:26px;text-align:center;background:linear-gradient(135deg,rgba(255,183,45,.20),rgba(255,141,26,.11));border:1px solid rgba(255,183,45,.35);border-radius:32px;padding:clamp(24px,6vw,46px)}.cta h2{font-size:clamp(34px,8vw,70px);line-height:1.02;margin:0 0 10px}.cta p{color:#f0e2c4;font-size:clamp(18px,4vw,25px);margin:0 0 20px}.button{display:inline-flex;background:var(--gold);color:#111;text-decoration:none;font-weight:900;border-radius:999px;padding:15px 22px;font-size:20px;box-shadow:0 14px 45px rgba(255,183,45,.25)}.button.disabled{opacity:.72;cursor:default}
'''

HEAD = '<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><meta name="theme-color" content="#07090c"/><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;600;700;800;900&family=Noto+Sans+Arabic:wght@400;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;600;700;800;900&display=swap" rel="stylesheet">'

for code, data in LANGS.items():
    links = ''.join(f'<a href="{c}.html" class="{"active" if c == code else ""}">{x["label"]}</a>' for c, x in LANGS.items())
    cards = ''.join(f'<div class="fit-card"><b>{t}</b><p>{body}</p></div>' for t, body in data['cards'])
    systems = ''.join(f'<span>{item}</span>' for item in data['systems'])
    html = f'''<!doctype html><html lang="{data['lang']}" dir="{data['dir']}"><head>{HEAD}<meta property="og:title" content="{data['title']}"/><meta property="og:description" content="{data['lead']}"/><meta property="og:image" content="https://kopcaptz.github.io/strauss-elite-energy-recruitment/assets/processed/02-pipe-platform-sketch-a.jpg"/><title>{data['title']}</title><style>{CSS}</style></head><body><main class="wrap"><nav class="lang-switch" aria-label="Language switch">{links}</nav><section class="hero"><img src="../assets/processed/02-pipe-platform-sketch-a.jpg" alt=""><div class="hero-content"><div class="eyebrow">{data['brand']}</div><h1>{data['title']}</h1><p class="lead">{data['lead']}</p><div class="systems">{systems}</div></div></section><section class="section-title"><h2>{data['section']}</h2><p>{data['section_p']}</p></section><section class="story"><article class="photo"><img src="../assets/processed/01-boiler-room-sketch.jpg" alt=""><div class="photo-content"><div class="topline">{data['boiler_top']}</div><div class="copybox"><h3>{data['boiler_t']}</h3><p>{data['boiler_p']}</p></div></div></article><article class="photo"><img src="../assets/processed/04-compressor-room-sketch.jpg" alt=""><div class="photo-content"><div class="topline">{data['comp_top']}</div><div class="copybox"><h3>{data['comp_t']}</h3><p>{data['comp_p']}</p></div></div></article></section><section class="section-title"><h2>{data['fit_t']}</h2><p>{data['fit_p']}</p></section><section class="fit">{cards}</section><section class="cta"><h2>{data['cta_t']}</h2><p>{data['cta_p']}</p><div class="button disabled" role="presentation" aria-disabled="true">{data['cta_b']}</div></section></main></body></html>'''
    (LANG_DIR / f'{code}.html').write_text(html)

(DOCS / 'multilingual.html').write_text('''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Choose language</title><style>body{min-height:100svh;margin:0;background:radial-gradient(circle at 70% 0%,rgba(255,183,45,.18),transparent 34%),#07090c;color:#fff8ea;font-family:Arial,sans-serif;display:grid;place-items:center;padding:24px}.box{max-width:720px;text-align:center}.links{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}.links a{background:#ffb72d;color:#111;text-decoration:none;border-radius:999px;padding:12px 16px;font-weight:800}</style></head><body><main class="box"><h1>Choose language</h1><p>בחרו שפה · اختر اللغة · Выберите язык · भाषा चुनें</p><nav class="links"><a href="lang/he.html">עברית</a><a href="lang/en.html">English</a><a href="lang/ar.html">العربية</a><a href="lang/ru.html">Русский</a><a href="lang/hi.html">हिन्दी</a></nav></main><script>const m={he:'he',ar:'ar',ru:'ru',hi:'hi',en:'en'};const l=(navigator.language||'').slice(0,2);if(location.search.includes('auto=1')&&m[l]) location.replace('lang/'+m[l]+'.html');</script></body></html>''')
print('wrote', ', '.join(sorted(p.name for p in LANG_DIR.glob('*.html'))))
