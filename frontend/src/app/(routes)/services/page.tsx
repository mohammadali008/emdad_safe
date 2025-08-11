export default function ServicesPage(){
  const items = [
    { t:'یدک‌کش و حمل خودرو', d:'حمل ایمن تا مقصد با خودروبر' },
    { t:'باتری‌به‌جا', d:'تعویض و باتری کمکی در محل' },
    { t:'پنچرگیری سیار', d:'تعمیر و تعویض تایر' },
    { t:'سوخت‌رسانی', d:'بنزین/گازوئیل در محل' },
    { t:'تعمیر در محل', d:'رفع عیب‌های متداول' },
  ];
  return (
    <section className="section"><div className="container">
      <h1 className="h4 fw-bold mb-4">خدمات امداد خودرو</h1>
      <div className="row g-3">
        {items.map((s,i)=> (
          <div className="col-12 col-md-6" key={i}>
            <div className="card p-3 h-100">
              <div className="fw-bold mb-1">{s.t}</div>
              <div className="text-muted">{s.d}</div>
            </div>
          </div>
        ))}
      </div>
    </div></section>
  );
}
