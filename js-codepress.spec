Summary:	Online Real Time Syntax Highlighting Editor
Name:		codepress
Version:	0.9.6
Release:	0.1
License:	LGPL 2.1
Group:		Applications/WWW
Source0:	http://www.codepress.org/download/%{name}-v.%{version}.zip
# Source0-md5:	7d682bfdeac92abcbd4fe5414342ae61
URL:		http://www.codepress.org/
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
CodePress is web-based source code editor with syntax highlighting
written in JavaScript that colors text in real time while it's being
typed in the browser.

Features
- Real-time syntax highlighting: just write some code
- Code snippets: on PHP example type "if" and press [tab]
- Auto completion: simple type " or ( or ' or [ or { on any example
  below (except Plain Text)
- Shortcuts: on PHP example press [ctrl][shift][space]. It's shortcut
  to &nbsp;
- Multiple windows: you can add multiple CodePress windows to the same
  page

%prep
%setup -qc
mv codepress/license.txt .
mv codepress/index.html .
find '(' -name '*.js' -o -name '*.html' -o -name '*.css' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a codepress/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc index.html
%{_appdir}
