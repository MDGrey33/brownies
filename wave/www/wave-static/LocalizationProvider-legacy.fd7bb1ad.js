System.register(["./vendor-legacy.6bd105bc.js","./useThemeProps-legacy.ef85bc10.js"],(function(e){"use strict";var t,n,o,a;return{setters:[function(e){t=e.bF,n=e.r},function(e){o=e.y,a=e.j}],execute:function(){e("L",(function(e){var r=o({props:e,name:"MuiLocalizationProvider"}),u=r.children,l=r.dateAdapter,s=r.dateFormats,d=r.dateLibInstance,m=r.locale,f=r.adapterLocale,p=r.localeText,x=n.exports.useMemo((function(){return new l({locale:null!=f?f:m,formats:s,instance:d})}),[l,m,f,s,d]),b=n.exports.useMemo((function(){return{minDate:x.date("1900-01-01T00:00:00.000"),maxDate:x.date("2099-12-31T00:00:00.000")}}),[x]),v=n.exports.useMemo((function(){return{utils:x,defaultDates:b,localeText:t({},c,null!=p?p:{})}}),[b,x,p]);return a.exports.jsx(i.Provider,{value:v,children:u})}));var r={previousMonth:"Previous month",nextMonth:"Next month",openPreviousView:"open previous view",openNextView:"open next view",calendarViewSwitchingButtonAriaLabel:function(e){return"year"===e?"year view is open, switch to calendar view":"calendar view is open, switch to year view"},start:"Start",end:"End",cancelButtonLabel:"Cancel",clearButtonLabel:"Clear",okButtonLabel:"OK",todayButtonLabel:"Today",clockLabelText:function(e,t,n){return"Select ".concat(e,". ").concat(null===t?"No time selected":"Selected time is ".concat(n.format(t,"fullTime")))},hoursClockNumberText:function(e){return"".concat(e," hours")},minutesClockNumberText:function(e){return"".concat(e," minutes")},secondsClockNumberText:function(e){return"".concat(e," seconds")},openDatePickerDialogue:function(e,t){return e&&t.isValid(t.date(e))?"Choose date, selected date is ".concat(t.format(t.date(e),"fullDate")):"Choose date"},openTimePickerDialogue:function(e,t){return e&&t.isValid(t.date(e))?"Choose time, selected time is ".concat(t.format(t.date(e),"fullTime")):"Choose time"},timeTableLabel:"pick time",dateTableLabel:"pick date"},c=r;t({},r);var i=e("M",n.exports.createContext(null))}}}));