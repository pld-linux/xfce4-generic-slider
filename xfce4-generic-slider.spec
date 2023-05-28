Summary:	Generic slider plugin for the Xfce4 Panel
Summary(pl.UTF-8):	Wtyczka ogólnego przeznaczenia dla panelu Xfce4
Name:		xfce4-generic-slider
Version:	1.0.0
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-generic-slider/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	4a599079f49bdf462049e38bcc802e55
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-generic-slider
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.14.0
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce4-generic-slider is a tool to help Xfce users deal with a variable
which they wish to both GET and SET. The getting side is similar to
what xfce4-genmon-plugin does except the command's numerical output is
represented visually in a slider. Dragging the slider is then used to
set the value through calls to a second command.

%description -l pl.UTF-8
Xfce4-generic-slider to narzędzie pomagające użytkownikom Xfce radzić
sobie ze zmienną, którą chcą zarówno GET, jak i SET. Pobieranie jest
podobne do tego, co robi xfce4-genmon-plugin, z wyjątkiem tego, że
numeryczne wyjście polecenia jest reprezentowane wizualnie na suwaku.
Przeciąganie suwaka jest następnie używane do ustawiania wartości
poprzez wywołania drugiego polecenia.

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libgeneric-slider.so
%{_datadir}/xfce4/panel/plugins/generic-slider.desktop
%{_iconsdir}/hicolor/*x*/apps/org.xfce.panel.genericslider.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.panel.genericslider.svg
