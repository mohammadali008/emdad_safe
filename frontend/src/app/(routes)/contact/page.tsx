export default function ContactPage(){
  return (
    <section className="section"><div className="container">
      <h1 className="h4 fw-bold mb-4">درخواست امداد</h1>
      <form className="row g-3" action="#" method="post">
        <div className="col-12 col-md-6">
          <label className="form-label">نام</label>
          <input className="form-control" name="name" required />
        </div>
        <div className="col-12 col-md-6">
          <label className="form-label">تلفن</label>
          <input className="form-control" name="phone" inputMode="tel" required />
        </div>
        <div className="col-12">
          <label className="form-label">آدرس/لوکیشن</label>
          <textarea className="form-control" name="address" rows={3} />
        </div>
        <div className="col-12 d-flex gap-2">
          <button className="btn btn-primary" type="submit">ثبت درخواست</button>
          <a className="btn btn-outline-secondary" href="tel:+982191300000">تماس تلفنی</a>
        </div>
      </form>
    </div></section>
  );
}
