export default function BlogPage(){
  const posts = [
    { t:'نکات مهم هنگام پنچر شدن در بزرگراه', d:'چگونه ایمن بمانیم و سریع مشکل را حل کنیم.' },
    { t:'علائم خرابی باتری و زمان تعویض', d:'۵ نشانه که می‌گوید وقت تعویض باتری رسیده.' },
  ];
  return (
    <section className="section"><div className="container">
      <h1 className="h4 fw-bold mb-4">وبلاگ</h1>
      <div className="row g-3">
        {posts.map((p,i)=> (
          <div className="col-12 col-md-6" key={i}>
            <div className="card p-3 h-100">
              <div className="fw-bold mb-1">{p.t}</div>
              <div className="text-muted">{p.d}</div>
            </div>
          </div>
        ))}
      </div>
    </div></section>
  );
}
