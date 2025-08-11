export default function FAQPage(){
  const faqs = [
    { q:'چقدر طول می‌کشد تا برسید؟', a:'در محدوده شهری معمولاً زیر ۳۰ دقیقه.' },
    { q:'هزینه‌ها چطور محاسبه می‌شود؟', a:'شفاف و طبق تعرفه—قبل از شروع کار اعلام می‌کنیم.' },
    { q:'پوشش شما شبانه‌روزی است؟', a:'بله، ۲۴ ساعته و ۷ روز هفته.' },
  ];
  return (
    <section className="section"><div className="container">
      <h1 className="h4 fw-bold mb-4">سوالات متداول</h1>
      <div className="accordion" id="faq">
        {faqs.map((f,i)=> (
          <div className="accordion-item" key={i}>
            <h2 className="accordion-header">
              <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target={`#c${i}`}>
                {f.q}
              </button>
            </h2>
            <div id={`c${i}`} className="accordion-collapse collapse" data-bs-parent="#faq">
              <div className="accordion-body">{f.a}</div>
            </div>
          </div>
        ))}
      </div>
    </div></section>
  );
}
