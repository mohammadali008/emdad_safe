export default function Footer() {
  return (
    <footer className="mt-5 pt-5 pb-4" style={{background:'var(--footer-bg)', color:'#eee'}}>
      <div className="container">
        <div className="row g-4">
          <div className="col-12 col-md-4">
            <h6 className="fw-bold mb-3 text-white">درباره ما</h6>
            <p className="text-light">امداد خودرو ۲۴ ساعته با پوشش شهری و بین‌شهری. تلاش ما ارائه سریع‌ترین خدمات با قیمت شفاف است.</p>
          </div>
          <div className="col-6 col-md-4">
            <h6 className="fw-bold mb-3 text-white">خدمات</h6>
            <ul className="list-unstyled m-0 p-0 d-grid gap-2">
              <li><a href="#" className="text-light">یدک‌کش و حمل خودرو</a></li>
              <li><a href="#" className="text-light">باتری‌به‌جا و برق اضطراری</a></li>
              <li><a href="#" className="text-light">پنچرگیری سیار</a></li>
              <li><a href="#" className="text-light">سوخت‌رسانی</a></li>
              <li><a href="#" className="text-light">تعمیر در محل</a></li>
            </ul>
          </div>
          <div className="col-6 col-md-4">
            <h6 className="fw-bold mb-3 text-white">تماس</h6>
            <address className="text-light m-0">تهران، خیابان مثال، پلاک ۱۲۳</address>
            <a href="tel:+982191300000" className="d-block mt-2 text-light">021-91300000</a>
            <a href="mailto:info@emdadsafe.example.com" className="d-block text-light">info@emdadsafe.example.com</a>
          </div>
        </div>
        <hr className="my-4 border-light" />
        <div className="d-flex justify-content-between small text-light">
          <span>© {new Date().getFullYear()} امداد سیف</span>
          <span>طراحی سبک و سئو شده با Next.js</span>
        </div>
      </div>
    </footer>
  );
}
