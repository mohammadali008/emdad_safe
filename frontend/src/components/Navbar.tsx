'use client';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useState } from 'react';

const NAV = [
  { href: '/', label: 'خانه' },
  { href: '/services', label: 'خدمات' },
  { href: '/blog', label: 'وبلاگ' },
  { href: '/faq', label: 'سوالات متداول' },
  { href: '/contact', label: 'تماس با ما' },
];

export default function Navbar() {
  const pathname = usePathname();
  const [open, setOpen] = useState(false);
  const isActive = (href: string) => (href === '/' ? pathname === '/' : pathname?.startsWith(href));

  return (
    <header
      className="shadow-sm position-sticky top-0"
      style={{ zIndex: 1000, background: 'var(--grad-hot)', color: '#fff' }}
    >
      <div className="container d-flex align-items-center justify-content-between py-2">
        {/* لوگو سمت راست */}
        <Link href="/" className="d-flex align-items-center gap-2 text-white">
          <img src="/logo.svg" alt="EmdadSafe" width={36} height={36} loading="eager" />
          <span className="fw-bold">امداد سیف</span>
        </Link>

        {/* منو برای دسکتاپ */}
        <nav className="d-none d-md-flex align-items-center justify-content-between w-100 ms-4">
          {/* لینک‌ها سمت راست */}
          <div className="d-flex gap-3">
            {NAV.filter(item => item.href !== '/contact').map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className={isActive(item.href) ? 'fw-bold text-white' : 'text-white'}
              >
                {item.label}
              </Link>
            ))}
          </div>

          {/* دکمه تماس با ما سمت چپ */}
          <Link href="/contact" className="btn btn-light btn-sm text-danger fw-bold">
            درخواست امداد
          </Link>
        </nav>

        {/* منو موبایل */}
        <button
          className="btn btn-sm d-md-none btn-light text-dark"
          aria-label="toggle"
          onClick={() => setOpen(!open)}
        >
          منو
        </button>
      </div>

      {/* منوی موبایل بازشونده */}
      {open && (
        <div className="container d-md-none pb-3">
          <div className="d-flex flex-column gap-2">
            {NAV.filter(item => item.href !== '/contact').map((item) => (
              <Link
                key={item.href}
                href={item.href}
                onClick={() => setOpen(false)}
                className={isActive(item.href) ? 'fw-bold text-white' : 'text-white'}
              >
                {item.label}
              </Link>
            ))}
            <Link href="/contact" className="btn btn-light text-danger fw-bold">
              درخواست امداد
            </Link>
          </div>
        </div>
      )}
    </header>
  );
}
