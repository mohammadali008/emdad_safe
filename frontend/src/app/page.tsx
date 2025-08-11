import Link from 'next/link';

export default function HomePage(){
  return (
    <>
      <section className="py-5" style={{ background: 'var(--grad-hot)', color:'#fff' }}>
        <div className="container d-flex flex-column flex-md-row align-items-center gap-4">
          <div className="flex-fill">
            <h1 className="display-6 fw-bold mb-3">امداد خودرو سریع، نزدیک شما</h1>
            <p className="mb-4">یدک‌کش، باتری‌به‌جا، پنچرگیری، سوخت‌رسانی و تعمیر در محل—شبانه‌روزی و قیمت شفاف.</p>
            <div className="d-flex gap-2 flex-wrap">
              <Link href="/contact" className="btn btn-light">درخواست امداد</Link>
              <Link href="/services" className="btn btn-outline-light">مشاهده خدمات</Link>
            </div>
          </div>
          <div className="flex-fill text-center">
            <img src="/hero-van.webp" alt="خودرو امدادی" width={420} height={280} loading="eager" />
          </div>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <div className="row g-3">
            {[
              { t: 'پاسخ کمتر از ۳۰ دقیقه', d: 'در محدوده شهری' },
              { t: 'قیمت شفاف', d: 'بدون هزینه پنهان' },
              { t: 'پوشش ۲۴/۷', d: 'شبانه‌روزی' },
              { t: 'تکنسین‌های متخصص', d: 'با ابزار کامل' },
            ].map((b,i)=> (
              <div className="col-6 col-md-3" key={i}>
                <div className="card p-3 h-100 text-center">
                  <div className="fw-bold mb-1">{b.t}</div>
                  <div className="text-muted small">{b.d}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
