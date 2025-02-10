/** @jsxImportSource @emotion/react */


import { ErrorBoundary } from "react-error-boundary"
import { Fragment, useCallback, useContext, useEffect, useRef, useState } from "react"
import { ColorModeContext, EventLoopContext, StateContexts } from "$/utils/context"
import { Event, getBackendURL, getRefValue, getRefValues, isTrue, refs } from "$/utils/state"
import { jsx, keyframes } from "@emotion/react"
import { AlignJustifyIcon as LucideAlignJustifyIcon, BookOpenCheckIcon as LucideBookOpenCheckIcon, BookUserIcon as LucideBookUserIcon, LibraryIcon as LucideLibraryIcon, LogOutIcon as LucideLogOutIcon, MoonIcon as LucideMoonIcon, SquarePlusIcon as LucideSquarePlusIcon, SunIcon as LucideSunIcon, TriangleAlertIcon as LucideTriangleAlertIcon, UserIcon as LucideUserIcon, WifiOffIcon as LucideWifiOffIcon, XIcon as LucideXIcon } from "lucide-react"
import { toast, Toaster } from "sonner"
import env from "$/env.json"
import { Box as RadixThemesBox, Button as RadixThemesButton, Callout as RadixThemesCallout, Card as RadixThemesCard, Flex as RadixThemesFlex, Heading as RadixThemesHeading, IconButton as RadixThemesIconButton, Link as RadixThemesLink, ScrollArea as RadixThemesScrollArea, Select as RadixThemesSelect, Separator as RadixThemesSeparator, Text as RadixThemesText, TextField as RadixThemesTextField, Theme as RadixThemesTheme } from "@radix-ui/themes"
import NextLink from "next/link"
import { Drawer as VaulDrawer } from "vaul"
import theme from "$/utils/theme.js"
import { GoogleLogin, GoogleOAuthProvider } from "@react-oauth/google"
import { Root as RadixFormRoot } from "@radix-ui/react-form"
import NextHead from "next/head"



const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Fragment_f2f0916d2fcc08b7cdf76cec697f0750 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    <Fragment>

{isTrue((connectErrors.length > 0)) ? (
  <Fragment>

<LucideWifiOffIcon css={({ ["color"] : "crimson", ["zIndex"] : 9999, ["position"] : "fixed", ["bottom"] : "33px", ["right"] : "33px", ["animation"] : (pulse+" 1s infinite") })} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Errorboundary_09b04aa4f8ea3f9caab62ce7f2edea06 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_error_0f5dbf674521530422d73a7946faf6d4 = useCallback(((_error, _info) => (addEvents([(Event("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception", ({ ["stack"] : _error["stack"], ["component_stack"] : _info["componentStack"] }), ({  })))], [_error, _info], ({  })))), [addEvents, Event])



  
  return (
    <ErrorBoundary fallbackRender={((event_args) => (jsx("div", ({ ["css"] : ({ ["height"] : "100%", ["width"] : "100%", ["position"] : "absolute", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" }) }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "1rem" }) }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "1rem", ["maxWidth"] : "50ch", ["border"] : "1px solid #888888", ["borderRadius"] : "0.25rem", ["padding"] : "1rem" }) }), (jsx("h2", ({ ["css"] : ({ ["fontSize"] : "1.25rem", ["fontWeight"] : "bold" }) }), (jsx(Fragment, ({  }), "An error occurred while rendering this page.")))), (jsx("p", ({ ["css"] : ({ ["opacity"] : "0.75" }) }), (jsx(Fragment, ({  }), "This is an error with the application itself.")))), (jsx("details", ({  }), (jsx("summary", ({ ["css"] : ({ ["padding"] : "0.5rem" }) }), (jsx(Fragment, ({  }), "Error message")))), (jsx("div", ({ ["css"] : ({ ["width"] : "100%", ["maxHeight"] : "50vh", ["overflow"] : "auto", ["background"] : "#000", ["color"] : "#fff", ["borderRadius"] : "0.25rem" }) }), (jsx("div", ({ ["css"] : ({ ["padding"] : "0.5rem", ["width"] : "fit-content" }) }), (jsx("pre", ({  }), (jsx(Fragment, ({  }), event_args.error.stack)))))))), (jsx("button", ({ ["css"] : ({ ["padding"] : "0.35rem 0.75rem", ["margin"] : "0.5rem", ["background"] : "#fff", ["color"] : "#000", ["border"] : "1px solid #000", ["borderRadius"] : "0.25rem", ["fontWeight"] : "bold" }), ["onClick"] : ((...args) => (addEvents([(Event("_call_function", ({ ["function"] : (() => (navigator["clipboard"]["writeText"](event_args.error.stack))), ["callback"] : null }), ({  })))], args, ({  })))) }), (jsx(Fragment, ({  }), "Copy")))))))), (jsx("hr", ({ ["css"] : ({ ["borderColor"] : "currentColor", ["opacity"] : "0.25" }) }))), (jsx("a", ({ ["href"] : "https://reflex.dev" }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["alignItems"] : "baseline", ["justifyContent"] : "center", ["fontFamily"] : "monospace", ["--default-font-family"] : "monospace", ["gap"] : "0.5rem" }) }), (jsx(Fragment, ({  }), "Built with ")), (jsx("svg", ({ ["css"] : ({ ["viewBox"] : "0 0 56 12", ["fill"] : "currentColor" }), ["height"] : "12", ["width"] : "56", ["xmlns"] : "http://www.w3.org/2000/svg" }), (jsx("path", ({ ["d"] : "M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z" }))), (jsx("path", ({ ["d"] : "M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z" }))), (jsx("path", ({ ["d"] : "M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z" }))), (jsx("path", ({ ["d"] : "M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z" }))), (jsx("path", ({ ["d"] : "M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z" }))), (jsx("path", ({ ["d"] : "M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z" }))))))))))))))} onError={on_error_0f5dbf674521530422d73a7946faf6d4}>

<Fragment>

<Div_602c14884fa2de27f522fe8f94374b02/>
<Toaster_6e6ebf8d7ce589d59b7d382fb7576edf/>
</Fragment>
<Fragment_4cdbef6a38be3ebdf022e4bb53bb3166/>
<NextHead>

<title>

{"Prdprf | Index"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</ErrorBoundary>
  )
}

export function Div_602c14884fa2de27f522fe8f94374b02 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    <div css={({ ["position"] : "fixed", ["width"] : "100vw", ["height"] : "0" })} title={("Connection Error: "+((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''))}>

<Fragment_f2f0916d2fcc08b7cdf76cec697f0750/>
</div>
  )
}

export function Fragment_4cdbef6a38be3ebdf022e4bb53bb3166 () {
  
  const reflex___state____state__prdprf___auth___state____my_local_auth_state = useContext(StateContexts.reflex___state____state__prdprf___auth___state____my_local_auth_state)
  const reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state = useContext(StateContexts.reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const { toggleColorMode } = useContext(ColorModeContext)
  const { resolvedColorMode } = useContext(ColorModeContext)
  const ref_my_content_area_el = useRef(null); refs["ref_my_content_area_el"] = ref_my_content_area_el;
  
                useEffect(() => {
                    ((...args) => (addEvents([(Event("reflex___state____state.prdprf___auth___state____my_local_auth_state.prdprf___auth___state____session_state.prdprf___articles___state____article_public_state.set_limit_and_reload", ({ ["new_limit"] : 20 }), ({  })))], args, ({  }))))()
                    return () => {
                        
                    }
                }, []);
  const reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state__prdprf___articles___state____article_public_state = useContext(StateContexts.reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state__prdprf___articles___state____article_public_state)
  const reflex___state____state__reflex_local_auth___local_auth____local_auth_state__reflex_local_auth___registration____registration_state = useContext(StateContexts.reflex___state____state__reflex_local_auth___local_auth____local_auth_state__reflex_local_auth___registration____registration_state)
  const reflex___state____state__prdprf___auth___state____select_class_state = useContext(StateContexts.reflex___state____state__prdprf___auth___state____select_class_state)
  const reflex___state____state__prdprf___auth___state____select_litera_state = useContext(StateContexts.reflex___state____state__prdprf___auth___state____select_litera_state)
  const ref_Имя = useRef(null); refs["ref_\u0418\u043c\u044f"] = ref_Имя;
  const ref_Фамилия = useRef(null); refs["ref_\u0424\u0430\u043c\u0438\u043b\u0438\u044f"] = ref_Фамилия;
  const ref_Почта = useRef(null); refs["ref_\u041f\u043e\u0447\u0442\u0430"] = ref_Почта;
  const ref_Пароль = useRef(null); refs["ref_\u041f\u0430\u0440\u043e\u043b\u044c"] = ref_Пароль;
  const ref_Подтверждение_пароля = useRef(null); refs["ref_\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435_\u043f\u0430\u0440\u043e\u043b\u044f"] = ref_Подтверждение_пароля;

  
    const handleSubmit_3b889fbe6ca06a554b6df65d59d6f24e = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...({ ["\u041f\u0430\u0440\u043e\u043b\u044c"] : getRefValue(refs["ref_\u041f\u0430\u0440\u043e\u043b\u044c"]), ["\u041f\u043e\u0447\u0442\u0430"] : getRefValue(refs["ref_\u041f\u043e\u0447\u0442\u0430"]), ["\u0424\u0430\u043c\u0438\u043b\u0438\u044f"] : getRefValue(refs["ref_\u0424\u0430\u043c\u0438\u043b\u0438\u044f"]), ["\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435_\u043f\u0430\u0440\u043e\u043b\u044f"] : getRefValue(refs["ref_\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435_\u043f\u0430\u0440\u043e\u043b\u044f"]), ["\u0418\u043c\u044f"] : getRefValue(refs["ref_\u0418\u043c\u044f"]) })};

        (((...args) => (addEvents([(Event("reflex___state____state.reflex_local_auth___local_auth____local_auth_state.prdprf___auth___state____my_register_state.handle_registration", ({ ["form_data"] : form_data }), ({  })))], args, ({  }))))());

        if (false) {
            $form.reset()
        }
    })
    




  
  return (
    <Fragment>

{isTrue(reflex___state____state__prdprf___auth___state____my_local_auth_state.is_authenticated) ? (
  <Fragment>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<RadixThemesBox css={({ ["background"] : "var(--accent-7)", ["padding"] : "1em", ["width"] : "100%" })}>

<RadixThemesBox css={({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "block" }) })}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center" })} direction={"row"} justify={"between"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center" })} direction={"row"} gap={"3"}>

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>

<NextLink href={"/"} passHref={true}>

<img css={({ ["width"] : "2.25em", ["height"] : "auto", ["borderRadius"] : "25%" })} src={"/logo.jpg"}/>
</NextLink>
</RadixThemesLink>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>

<NextLink href={"/"} passHref={true}>

<RadixThemesHeading size={"7"} weight={"bold"}>

{"It-\u043f\u043e\u043b\u0438\u0433\u043e\u043d"}
</RadixThemesHeading>
</NextLink>
</RadixThemesLink>
</RadixThemesFlex>
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} gap={"5"}>

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/articles"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"column"} gap={"3"}>

<LucideLibraryIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
<Fragment>

{isTrue(reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_teacher) ? (
  <Fragment>

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/lessons"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"column"} gap={"3"}>

<LucideBookUserIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0412\u0430\u0448\u0438 \u0443\u0440\u043e\u043a\u0438"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
<Fragment>

{isTrue(reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_teacher) ? (
  <Fragment>

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/all_tests/add"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"column"} gap={"3"}>

<LucideSquarePlusIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u043d\u0438\u0435"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/all_tests"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"column"} gap={"3"}>

<LucideBookOpenCheckIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0417\u0430\u0434\u0430\u043d\u0438\u044f"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
</RadixThemesFlex>
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} justify={"end"} gap={"4"}>

<RadixThemesBox css={({ ["as"] : "button", ["underline"] : "none", ["weight"] : "medium", ["width"] : "100%" })} onClick={((...args) => (addEvents([(Event("reflex___state____state.prdprf___navigation___state____nav_state.to_logout", ({  }), ({  })))], args, ({  }))))}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["cursor"] : "pointer", ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["color"] : "var(--accent-11)", ["border-radius"] : "0.5em", ["width"] : "100%", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem" })} direction={"row"} gap={"3"}>

<LucideLogOutIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText as={"p"} size={"4"}>

{""}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesBox>
<RadixThemesBox css={({ ["as"] : "button", ["underline"] : "none", ["weight"] : "medium", ["width"] : "100%" })} onClick={toggleColorMode}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["cursor"] : "pointer", ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["color"] : "var(--accent-11)", ["border-radius"] : "0.5em", ["width"] : "100%", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem" })} direction={"row"} gap={"3"}>

<Fragment>

{isTrue((resolvedColorMode === "light")) ? (
  <Fragment>

<LucideMoonIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
) : (
  <Fragment>

<LucideSunIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
)}
</Fragment>
</RadixThemesFlex>
</RadixThemesBox>
<Fragment>

{isTrue(reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_user_info) ? (
  <Fragment>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["width"] : "100%" })} direction={"row"} justify={"start"} gap={"3"}>

<RadixThemesIconButton css={({ ["padding"] : "6px" })} onClick={((...args) => (addEvents([(Event("_redirect", ({ ["path"] : "/profile", ["external"] : false, ["replace"] : false }), ({  })))], args, ({  }))))} radius={"full"} size={"4"}>

<LucideUserIcon css={({ ["color"] : "var(--current-color)" })} size={48}/>
</RadixThemesIconButton>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"column"} justify={"start"} gap={"0"}>

<RadixThemesBox css={({ ["width"] : "85%" })}>

<RadixThemesText as={"p"} size={"3"} weight={"bold"}>

{(((isTrue(reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_username) ? reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_username : "\u0418\u043c\u044f")+" ")+(isTrue(reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_surname) ? reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_surname : "\u0424\u0430\u043c\u0438\u043b\u0438\u044f"))}
</RadixThemesText>
<RadixThemesFlex css={({ ["overflow"] : "hidden" })}>

<RadixThemesText as={"p"} size={"2"} weight={"medium"}>

{reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_user_info?.["email"]}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesFlex>
</Fragment>
) : (
  <Fragment>

{""}
</Fragment>
)}
</Fragment>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesBox>
<RadixThemesBox css={({ ["padding"] : "1em", ["@media screen and (min-width: 0)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "none" }) })}>

<VaulDrawer.Root direction={"left"}>

<VaulDrawer.Trigger asChild={true}>

<LucideAlignJustifyIcon css={({ ["color"] : "var(--current-color)" })} size={30}/>
</VaulDrawer.Trigger>
<VaulDrawer.Overlay css={({ ["position"] : "fixed", ["left"] : "0", ["right"] : "0", ["bottom"] : "0", ["top"] : "0", ["z_index"] : 50, ["background"] : "rgba(0, 0, 0, 0.5)", ["zIndex"] : "5" })}/>
<VaulDrawer.Portal css={({ ["width"] : "100%" })}>

<RadixThemesTheme css={{...theme.styles.global[':root'], ...theme.styles.global.body}}>

<VaulDrawer.Content css={({ ["left"] : "0", ["right"] : "auto", ["bottom"] : "0", ["top"] : "auto", ["position"] : "fixed", ["z_index"] : 50, ["display"] : "flex", ["height"] : "100%", ["width"] : "20em", ["padding"] : "1.5em", ["background"] : "var(--accent-2)" })}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"column"} gap={"5"}>

<RadixThemesBox css={({ ["width"] : "100%" })}>

<VaulDrawer.Close asChild={true}>

<LucideXIcon css={({ ["color"] : "var(--current-color)" })} size={30}/>
</VaulDrawer.Close>
</RadixThemesBox>
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/articles"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"row"} gap={"3"}>

<LucideLibraryIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/all_tests"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"row"} gap={"3"}>

<LucideBookOpenCheckIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0422\u0435\u0441\u0442\u044b"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
<Fragment>

{isTrue(reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_teacher) ? (
  <Fragment>

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/lessons"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"row"} gap={"3"}>

<LucideBookUserIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0412\u0430\u0448\u0438 \u0443\u0440\u043e\u043a\u0438"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
<Fragment>

{isTrue(reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_teacher) ? (
  <Fragment>

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/all_tests/add"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"row"} gap={"3"}>

<LucideSquarePlusIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u043d\u0438\u0435"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/all_tests"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"row"} gap={"3"}>

<LucideBookOpenCheckIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0417\u0430\u0434\u0430\u043d\u0438\u044f"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
</RadixThemesFlex>
<RadixThemesFlex css={({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })}/>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"column"} gap={"5"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"column"} gap={"1"}>

<RadixThemesBox css={({ ["as"] : "button", ["underline"] : "none", ["weight"] : "medium", ["width"] : "100%" })} onClick={toggleColorMode}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["cursor"] : "pointer", ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["color"] : "var(--accent-11)", ["border-radius"] : "0.5em", ["width"] : "100%", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem" })} direction={"row"} gap={"3"}>

<Fragment>

{isTrue((resolvedColorMode === "light")) ? (
  <Fragment>

<LucideMoonIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
) : (
  <Fragment>

<LucideSunIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
)}
</Fragment>
</RadixThemesFlex>
</RadixThemesBox>
<RadixThemesBox css={({ ["as"] : "button", ["underline"] : "none", ["weight"] : "medium", ["width"] : "100%" })} onClick={((...args) => (addEvents([(Event("reflex___state____state.prdprf___navigation___state____nav_state.to_logout", ({  }), ({  })))], args, ({  }))))}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["cursor"] : "pointer", ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["color"] : "var(--accent-11)", ["border-radius"] : "0.5em", ["width"] : "100%", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem" })} direction={"row"} gap={"3"}>

<LucideLogOutIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText as={"p"} size={"4"}>

{"\u0412\u044b\u0439\u0442\u0438"}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesFlex>
<RadixThemesSeparator css={({ ["margin"] : "0" })} size={"4"}/>
<Fragment>

{isTrue(reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_user_info) ? (
  <Fragment>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["width"] : "100%" })} direction={"row"} justify={"start"} gap={"3"}>

<RadixThemesIconButton css={({ ["padding"] : "6px" })} onClick={((...args) => (addEvents([(Event("_redirect", ({ ["path"] : "/profile", ["external"] : false, ["replace"] : false }), ({  })))], args, ({  }))))} radius={"full"} size={"4"}>

<LucideUserIcon css={({ ["color"] : "var(--current-color)" })} size={48}/>
</RadixThemesIconButton>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"column"} justify={"start"} gap={"0"}>

<RadixThemesBox css={({ ["width"] : "85%" })}>

<RadixThemesText as={"p"} size={"3"} weight={"bold"}>

{(((isTrue(reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_username) ? reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_username : "\u0418\u043c\u044f")+" ")+(isTrue(reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_surname) ? reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_surname : "\u0424\u0430\u043c\u0438\u043b\u0438\u044f"))}
</RadixThemesText>
<RadixThemesFlex css={({ ["overflow"] : "hidden" })}>

<RadixThemesText as={"p"} size={"2"} weight={"medium"}>

{reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state.authenticated_user_info?.["email"]}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesFlex>
</Fragment>
) : (
  <Fragment>

{""}
</Fragment>
)}
</Fragment>
</RadixThemesFlex>
</RadixThemesFlex>
</VaulDrawer.Content>
</RadixThemesTheme>
</VaulDrawer.Portal>
</VaulDrawer.Root>
</RadixThemesBox>
</RadixThemesBox>
<RadixThemesBox css={({ ["padding"] : "1em", ["width"] : "100%" })} id={"my-content-area-el"} ref={ref_my_content_area_el}>

<RadixThemesBox css={({ ["minHeight"] : "85vh" })}>

<RadixThemesHeading size={"2"}>

{"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432\u043d\u043e\u0432\u044c"}
</RadixThemesHeading>
<RadixThemesSeparator css={({ ["marginTop"] : "1em", ["marginBottom"] : "1em" })} size={"4"}/>
<RadixThemesScrollArea css={({ ["height"] : 700 })} scrollbars={"vertical"} type={"always"}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["columns"] : "3" })} direction={"column"} gap={"5"}>

<>{reflex___state____state__prdprf___auth___state____my_local_auth_state__prdprf___auth___state____session_state__prdprf___articles___state____article_public_state.posts.map((post, index_3810f147a017e2ae) => (
  <RadixThemesCard asChild={true} key={index_3810f147a017e2ae}>

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>

<NextLink href={("/articles/"+post["id"])} passHref={true}>

<RadixThemesFlex gap={"2"}>

<RadixThemesBox>

<RadixThemesHeading>

{post["title"]}
</RadixThemesHeading>
</RadixThemesBox>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
</RadixThemesCard>
))}</>
</RadixThemesFlex>
</RadixThemesScrollArea>
</RadixThemesBox>
<RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%" })}>

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} size={"3"}>

<NextLink href={"https://reflex.dev"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["textAlign"] : "center", ["padding"] : "1em" })} direction={"row"} gap={"3"}>

{"Built with "}
<svg css={({ ["viewBox"] : "0 0 56 12", ["fill"] : ((resolvedColorMode === "light") ? "#110F1F" : "white") })} height={"12"} width={"56"} xmlns={"http://www.w3.org/2000/svg"}>

<path d={"M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z"}/>
<path d={"M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z"}/>
<path d={"M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z"}/>
<path d={"M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z"}/>
<path d={"M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z"}/>
<path d={"M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z"}/>
</svg>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesFlex>
</Fragment>
) : (
  <Fragment>

<RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "85vh" })}>

<Fragment>

{isTrue(reflex___state____state__reflex_local_auth___local_auth____local_auth_state__reflex_local_auth___registration____registration_state.success) ? (
  <Fragment>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<RadixThemesText as={"p"}>

{"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u043f\u0440\u043e\u0448\u043b\u0430 \u0443\u0441\u043f\u0435\u0448\u043d\u043e!"}
</RadixThemesText>
</RadixThemesFlex>
</Fragment>
) : (
  <Fragment>

<RadixThemesCard>

<GoogleOAuthProvider clientId={""}>

<RadixFormRoot className={"Root "} css={({ ["width"] : "100%" })} onSubmit={handleSubmit_3b889fbe6ca06a554b6df65d59d6f24e}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["minWidth"] : "50vw" })} direction={"column"} gap={"3"}>

<RadixThemesHeading size={"7"}>

{"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442"}
</RadixThemesHeading>
<Fragment>

{isTrue(!((reflex___state____state__reflex_local_auth___local_auth____local_auth_state__reflex_local_auth___registration____registration_state.error_message === ""))) ? (
  <Fragment>

<RadixThemesCallout.Root color={"red"} css={({ ["icon"] : "triangle_alert", ["width"] : "100%" })} role={"alert"}>

<RadixThemesCallout.Icon>

<LucideTriangleAlertIcon css={({ ["color"] : "var(--current-color)" })}/>
</RadixThemesCallout.Icon>
<RadixThemesCallout.Text>

{reflex___state____state__reflex_local_auth___local_auth____local_auth_state__reflex_local_auth___registration____registration_state.error_message}
</RadixThemesCallout.Text>
</RadixThemesCallout.Root>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
<RadixThemesTextField.Root css={({ ["width"] : "100%" })} id={"\u0418\u043c\u044f"} name={"\u0418\u043c\u044f"} placeholder={"\u0418\u043c\u044f"} ref={ref_Имя} type={"username"}/>
<RadixThemesTextField.Root css={({ ["width"] : "100%" })} id={"\u0424\u0430\u043c\u0438\u043b\u0438\u044f"} name={"\u0424\u0430\u043c\u0438\u043b\u0438\u044f"} placeholder={"\u0424\u0430\u043c\u0438\u043b\u0438\u044f"} ref={ref_Фамилия} type={"surname"}/>
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} gap={"3"}>

<RadixThemesText as={"p"}>

{"\u041a\u043b\u0430\u0441\u0441 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f"}
</RadixThemesText>
<RadixThemesSelect.Root name={"grade"} onValueChange={((_ev_0) => (addEvents([(Event("reflex___state____state.prdprf___auth___state____select_class_state.change_value", ({ ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  }))))} value={reflex___state____state__prdprf___auth___state____select_class_state.value}>

<RadixThemesSelect.Trigger/>
<RadixThemesSelect.Content>

<RadixThemesSelect.Group>

{""}
<RadixThemesSelect.Item value={"7"}>

{"7"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"8"}>

{"8"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"9"}>

{"9"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"10"}>

{"10"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"11"}>

{"11"}
</RadixThemesSelect.Item>
</RadixThemesSelect.Group>
</RadixThemesSelect.Content>
</RadixThemesSelect.Root>
<RadixThemesText as={"p"}>

{"\u0411\u0443\u043a\u0432\u0430"}
</RadixThemesText>
<RadixThemesSelect.Root name={"litera"} onValueChange={((_ev_0) => (addEvents([(Event("reflex___state____state.prdprf___auth___state____select_litera_state.change_value", ({ ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  }))))} value={reflex___state____state__prdprf___auth___state____select_litera_state.value}>

<RadixThemesSelect.Trigger/>
<RadixThemesSelect.Content>

<RadixThemesSelect.Group>

{""}
<RadixThemesSelect.Item value={"\u0410"}>

{"\u0410"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"\u0411"}>

{"\u0411"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"\u0412"}>

{"\u0412"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"\u0413"}>

{"\u0413"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"\u0414"}>

{"\u0414"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"\u0415"}>

{"\u0415"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"\u041c"}>

{"\u041c"}
</RadixThemesSelect.Item>
</RadixThemesSelect.Group>
</RadixThemesSelect.Content>
</RadixThemesSelect.Root>
</RadixThemesFlex>
<RadixThemesTextField.Root css={({ ["width"] : "100%" })} id={"\u041f\u043e\u0447\u0442\u0430"} name={"\u041f\u043e\u0447\u0442\u0430"} placeholder={"\u041f\u043e\u0447\u0442\u0430"} ref={ref_Почта} type={"email"}/>
<RadixThemesTextField.Root css={({ ["width"] : "100%" })} id={"\u041f\u0430\u0440\u043e\u043b\u044c"} name={"\u041f\u0430\u0440\u043e\u043b\u044c"} placeholder={"\u041f\u0430\u0440\u043e\u043b\u044c"} ref={ref_Пароль} type={"password"}/>
<RadixThemesTextField.Root css={({ ["width"] : "100%" })} id={"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f"} name={"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f"} placeholder={"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435 \u041f\u0430\u0440\u043e\u043b\u044f"} ref={ref_Подтверждение_пароля} type={"confirm_password"}/>
<RadixThemesButton css={({ ["width"] : "100%" })}>

{"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f"}
</RadixThemesButton>
<RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%" })}>

<RadixThemesLink css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} href={"#"} onClick={((...args) => (addEvents([(Event("_redirect", ({ ["path"] : "/login", ["external"] : false, ["replace"] : false }), ({  })))], args, ({  }))))}>

{"\u0412\u043e\u0439\u0442\u0438 \u0432 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439 \u0430\u043a\u043a\u0430\u0443\u043d\u0442"}
</RadixThemesLink>
</RadixThemesFlex>
<RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%" })}>

<GoogleLogin onSuccess={((_data) => (addEvents([(Event("reflex___state____state.reflex_local_auth___local_auth____local_auth_state.prdprf___auth___state____my_register_state.handle_google_reg", ({ ["token_id"] : _data }), ({  })))], [_data], ({  }))))}/>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixFormRoot>
</GoogleOAuthProvider>
</RadixThemesCard>
</Fragment>
)}
</Fragment>
</RadixThemesFlex>
</Fragment>
)}
</Fragment>
  )
}

export function Toaster_6e6ebf8d7ce589d59b7d382fb7576edf () {
  
  const { resolvedColorMode } = useContext(ColorModeContext)

  refs['__toast'] = toast
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const toast_props = ({ ["description"] : ("Check if server is reachable at "+getBackendURL(env.EVENT).href), ["closeButton"] : true, ["duration"] : 120000, ["id"] : "websocket-error" });
  const [userDismissed, setUserDismissed] = useState(false);
  (useEffect(
() => {
    if ((connectErrors.length >= 2)) {
        if (!userDismissed) {
            toast.error(
                `Cannot connect to server: ${((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : '')}.`,
                {...toast_props, onDismiss: () => setUserDismissed(true)},
            )
        }
    } else {
        toast.dismiss("websocket-error");
        setUserDismissed(false);  // after reconnection reset dismissed state
    }
}
, [connectErrors]))




  
  return (
    <Toaster closeButton={false} expand={true} position={"bottom-right"} richColors={true} theme={resolvedColorMode}/>
  )
}

export default function Component() {
    




  return (
    <Errorboundary_09b04aa4f8ea3f9caab62ce7f2edea06/>
  )
}
