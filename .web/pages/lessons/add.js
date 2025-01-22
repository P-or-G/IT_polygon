/** @jsxImportSource @emotion/react */


import { ErrorBoundary } from "react-error-boundary"
import { Fragment, useCallback, useContext, useEffect, useRef, useState } from "react"
import { ColorModeContext, EventLoopContext, StateContexts } from "$/utils/context"
import { Event, getBackendURL, getRefValue, getRefValues, isTrue, refs } from "$/utils/state"
import { jsx, keyframes } from "@emotion/react"
import { AlignJustifyIcon as LucideAlignJustifyIcon, BookUserIcon as LucideBookUserIcon, LibraryIcon as LucideLibraryIcon, LogOutIcon as LucideLogOutIcon, MenuIcon as LucideMenuIcon, MoonIcon as LucideMoonIcon, NotebookPenIcon as LucideNotebookPenIcon, PhoneIcon as LucidePhoneIcon, ScrollTextIcon as LucideScrollTextIcon, SunIcon as LucideSunIcon, UserIcon as LucideUserIcon, WifiOffIcon as LucideWifiOffIcon, XIcon as LucideXIcon } from "lucide-react"
import { toast, Toaster } from "sonner"
import env from "$/env.json"
import { Box as RadixThemesBox, Button as RadixThemesButton, DropdownMenu as RadixThemesDropdownMenu, Flex as RadixThemesFlex, Heading as RadixThemesHeading, IconButton as RadixThemesIconButton, Link as RadixThemesLink, Separator as RadixThemesSeparator, Text as RadixThemesText, TextArea as RadixThemesTextArea, TextField as RadixThemesTextField, Theme as RadixThemesTheme } from "@radix-ui/themes"
import NextLink from "next/link"
import { Drawer as VaulDrawer } from "vaul"
import theme from "$/utils/theme.js"
import { Root as RadixFormRoot } from "@radix-ui/react-form"
import NextHead from "next/head"



export function Div_602c14884fa2de27f522fe8f94374b02 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    <div css={({ ["position"] : "fixed", ["width"] : "100vw", ["height"] : "0" })} title={("Connection Error: "+((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''))}>

<Fragment_f2f0916d2fcc08b7cdf76cec697f0750/>
</div>
  )
}

export function Errorboundary_50c24ff147beb0d8cf78317c90541a63 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_error_0f5dbf674521530422d73a7946faf6d4 = useCallback(((_error, _info) => (addEvents([(Event("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception", ({ ["stack"] : _error["stack"], ["component_stack"] : _info["componentStack"] }), ({  })))], [_error, _info], ({  })))), [addEvents, Event])



  
  return (
    <ErrorBoundary fallbackRender={((event_args) => (jsx("div", ({ ["css"] : ({ ["height"] : "100%", ["width"] : "100%", ["position"] : "absolute", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" }) }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "1rem" }) }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "1rem", ["maxWidth"] : "50ch", ["border"] : "1px solid #888888", ["borderRadius"] : "0.25rem", ["padding"] : "1rem" }) }), (jsx("h2", ({ ["css"] : ({ ["fontSize"] : "1.25rem", ["fontWeight"] : "bold" }) }), (jsx(Fragment, ({  }), "An error occurred while rendering this page.")))), (jsx("p", ({ ["css"] : ({ ["opacity"] : "0.75" }) }), (jsx(Fragment, ({  }), "This is an error with the application itself.")))), (jsx("details", ({  }), (jsx("summary", ({ ["css"] : ({ ["padding"] : "0.5rem" }) }), (jsx(Fragment, ({  }), "Error message")))), (jsx("div", ({ ["css"] : ({ ["width"] : "100%", ["maxHeight"] : "50vh", ["overflow"] : "auto", ["background"] : "#000", ["color"] : "#fff", ["borderRadius"] : "0.25rem" }) }), (jsx("div", ({ ["css"] : ({ ["padding"] : "0.5rem", ["width"] : "fit-content" }) }), (jsx("pre", ({  }), (jsx(Fragment, ({  }), event_args.error.stack)))))))), (jsx("button", ({ ["css"] : ({ ["padding"] : "0.35rem 0.75rem", ["margin"] : "0.5rem", ["background"] : "#fff", ["color"] : "#000", ["border"] : "1px solid #000", ["borderRadius"] : "0.25rem", ["fontWeight"] : "bold" }), ["onClick"] : ((...args) => (addEvents([(Event("_call_function", ({ ["function"] : (() => (navigator["clipboard"]["writeText"](event_args.error.stack))), ["callback"] : null }), ({  })))], args, ({  })))) }), (jsx(Fragment, ({  }), "Copy")))))))), (jsx("hr", ({ ["css"] : ({ ["borderColor"] : "currentColor", ["opacity"] : "0.25" }) }))), (jsx("a", ({ ["href"] : "https://reflex.dev" }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["alignItems"] : "baseline", ["justifyContent"] : "center", ["fontFamily"] : "monospace", ["--default-font-family"] : "monospace", ["gap"] : "0.5rem" }) }), (jsx(Fragment, ({  }), "Built with ")), (jsx("svg", ({ ["css"] : ({ ["viewBox"] : "0 0 56 12", ["fill"] : "currentColor" }), ["height"] : "12", ["width"] : "56", ["xmlns"] : "http://www.w3.org/2000/svg" }), (jsx("path", ({ ["d"] : "M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z" }))), (jsx("path", ({ ["d"] : "M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z" }))), (jsx("path", ({ ["d"] : "M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z" }))), (jsx("path", ({ ["d"] : "M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z" }))), (jsx("path", ({ ["d"] : "M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z" }))), (jsx("path", ({ ["d"] : "M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z" }))))))))))))))} onError={on_error_0f5dbf674521530422d73a7946faf6d4}>

<Fragment>

<Div_602c14884fa2de27f522fe8f94374b02/>
<Toaster_6e6ebf8d7ce589d59b7d382fb7576edf/>
</Fragment>
<Fragment>

<Fragment_306dfa5d828ad878674eecb9ee7ccb36/>
</Fragment>
<NextHead>

<title>

{"Prdprf | Add"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</ErrorBoundary>
  )
}

export function Fragment_306dfa5d828ad878674eecb9ee7ccb36 () {
  
  const reflex___state____state = useContext(StateContexts.reflex___state____state)
  const reflex___state____state__reflex_local_auth___local_auth____local_auth_state = useContext(StateContexts.reflex___state____state__reflex_local_auth___local_auth____local_auth_state)
  const { toggleColorMode } = useContext(ColorModeContext)
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const { resolvedColorMode } = useContext(ColorModeContext)
  const reflex___state____state__reflex_local_auth___local_auth____local_auth_state__prdprf___auth___state____session_state = useContext(StateContexts.reflex___state____state__reflex_local_auth___local_auth____local_auth_state__prdprf___auth___state____session_state)
  const ref_my_content_area_el = useRef(null); refs["ref_my_content_area_el"] = ref_my_content_area_el;
  const ref_my_main_nav = useRef(null); refs["ref_my_main_nav"] = ref_my_main_nav;
  const ref_my_navbar_hstack_desktop = useRef(null); refs["ref_my_navbar_hstack_desktop"] = ref_my_navbar_hstack_desktop;
  
                useEffect(() => {
                    ((...args) => (addEvents([(Event("reflex___state____state.reflex_local_auth___local_auth____local_auth_state.reflex_local_auth___login____login_state.redir", ({  }), ({  })))], args, ({  }))))()
                    return () => {
                        
                    }
                }, []);

  
    const handleSubmit_9a2c705e13b955efed21c41fe61e2381 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...({  })};

        (((...args) => (addEvents([(Event("reflex___state____state.reflex_local_auth___local_auth____local_auth_state.prdprf___auth___state____session_state.prdprf___lessons___state____blog_post_state.prdprf___lessons___state____blog_add_post_form_state.handle_submit", ({ ["form_data"] : form_data }), ({  })))], args, ({  }))))());

        if (true) {
            $form.reset()
        }
    })
    




  
  return (
    <Fragment>

{isTrue((reflex___state____state.is_hydrated && reflex___state____state__reflex_local_auth___local_auth____local_auth_state.is_authenticated)) ? (
  <Fragment>

{isTrue(reflex___state____state__reflex_local_auth___local_auth____local_auth_state.is_authenticated) ? (
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

{"\u0423\u0440\u043e\u043a\u0438"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
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
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/lessons/add"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"column"} gap={"3"}>

<LucideNotebookPenIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0443\u0440\u043e\u043a"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/contact"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"column"} gap={"3"}>

<LucidePhoneIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u041e\u0431\u0440\u0430\u0442\u043d\u0430\u044f \u0441\u0432\u044f\u0437\u044c"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/contact/entries"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"column"} gap={"3"}>

<LucideScrollTextIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u041e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
</RadixThemesFlex>
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} justify={"end"} gap={"4"}>

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

{isTrue(reflex___state____state__reflex_local_auth___local_auth____local_auth_state__prdprf___auth___state____session_state.authenticated_user_info) ? (
  <Fragment>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["width"] : "100%" })} direction={"row"} justify={"start"} gap={"3"}>

<RadixThemesIconButton css={({ ["padding"] : "6px" })} radius={"full"} size={"4"}>

<LucideUserIcon css={({ ["color"] : "var(--current-color)" })} size={48}/>
</RadixThemesIconButton>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"column"} justify={"start"} gap={"0"}>

<RadixThemesBox css={({ ["width"] : "85%" })}>

<RadixThemesText as={"p"} size={"3"} weight={"bold"}>

{(isTrue(reflex___state____state__reflex_local_auth___local_auth____local_auth_state__prdprf___auth___state____session_state.authenticated_username) ? reflex___state____state__reflex_local_auth___local_auth____local_auth_state__prdprf___auth___state____session_state.authenticated_username : "\u0410\u043a\u043a\u0430\u0443\u043d\u0442")}
</RadixThemesText>
<RadixThemesFlex css={({ ["overflow"] : "hidden" })}>

<RadixThemesText as={"p"} size={"2"} weight={"medium"}>

{reflex___state____state__reflex_local_auth___local_auth____local_auth_state__prdprf___auth___state____session_state.authenticated_user_info?.["email"]}
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
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} gap={"5"}>

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/articles"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"column"} gap={"3"}>

<LucideLibraryIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0423\u0440\u043e\u043a\u0438"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
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
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/lessons/add"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"column"} gap={"3"}>

<LucideNotebookPenIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0443\u0440\u043e\u043a"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/contact"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"column"} gap={"3"}>

<LucidePhoneIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u041e\u0431\u0440\u0430\u0442\u043d\u0430\u044f \u0441\u0432\u044f\u0437\u044c"}
</RadixThemesText>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} underline={"none"} weight={"medium"}>

<NextLink href={"/contact/entries"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["&:hover"] : ({ ["background"] : "var(--accent-4)", ["color"] : "var(--accent-11)" }), ["border-radius"] : "0.5em", ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["paddingTop"] : "0.75rem", ["paddingBottom"] : "0.75rem", ["alignItems"] : "center" })} direction={"column"} gap={"3"}>

<LucideScrollTextIcon css={({ ["color"] : "var(--current-color)" })}/>
<RadixThemesText align={"center"} as={"p"} size={"4"} weight={"medium"}>

{"\u041e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f"}
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

{isTrue(reflex___state____state__reflex_local_auth___local_auth____local_auth_state__prdprf___auth___state____session_state.authenticated_user_info) ? (
  <Fragment>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["paddingInlineStart"] : "0.5rem", ["paddingInlineEnd"] : "0.5rem", ["width"] : "100%" })} direction={"row"} justify={"start"} gap={"3"}>

<RadixThemesIconButton css={({ ["padding"] : "6px" })} radius={"full"} size={"4"}>

<LucideUserIcon css={({ ["color"] : "var(--current-color)" })} size={48}/>
</RadixThemesIconButton>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"column"} justify={"start"} gap={"0"}>

<RadixThemesBox css={({ ["width"] : "85%" })}>

<RadixThemesText as={"p"} size={"3"} weight={"bold"}>

{(isTrue(reflex___state____state__reflex_local_auth___local_auth____local_auth_state__prdprf___auth___state____session_state.authenticated_username) ? reflex___state____state__reflex_local_auth___local_auth____local_auth_state__prdprf___auth___state____session_state.authenticated_username : "\u0410\u043a\u043a\u0430\u0443\u043d\u0442")}
</RadixThemesText>
<RadixThemesFlex css={({ ["overflow"] : "hidden" })}>

<RadixThemesText as={"p"} size={"2"} weight={"medium"}>

{reflex___state____state__reflex_local_auth___local_auth____local_auth_state__prdprf___auth___state____session_state.authenticated_user_info?.["email"]}
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

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["minHeight"] : "95vh" })} direction={"column"} gap={"5"}>

<RadixThemesHeading size={"9"}>

{"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0443\u0440\u043e\u043a"}
</RadixThemesHeading>
<RadixThemesBox css={({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "block" }) })}>

<RadixThemesBox css={({ ["width"] : "50vw" })}>

<RadixFormRoot className={"Root "} css={({ ["width"] : "100%" })} onSubmit={handleSubmit_9a2c705e13b955efed21c41fe61e2381}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"row"} gap={"3"}>

<RadixThemesTextField.Root css={({ ["width"] : "100%" })} name={"title"} placeholder={"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a"} required={true} type={"text"}/>
</RadixThemesFlex>
<RadixThemesTextArea css={({ ["height"] : "50vh", ["width"] : "100%" })} name={"content"} placeholder={"\u0412\u0430\u0448\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435"} required={true}/>
<RadixThemesButton type={"submit"}>

{"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c"}
</RadixThemesButton>
</RadixThemesFlex>
</RadixFormRoot>
</RadixThemesBox>
</RadixThemesBox>
<RadixThemesBox css={({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "none" }) })}>

<RadixThemesBox css={({ ["width"] : "75vw" })}>

<RadixFormRoot className={"Root "} css={({ ["width"] : "100%" })} onSubmit={handleSubmit_9a2c705e13b955efed21c41fe61e2381}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"row"} gap={"3"}>

<RadixThemesTextField.Root css={({ ["width"] : "100%" })} name={"title"} placeholder={"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a"} required={true} type={"text"}/>
</RadixThemesFlex>
<RadixThemesTextArea css={({ ["height"] : "50vh", ["width"] : "100%" })} name={"content"} placeholder={"\u0412\u0430\u0448\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435"} required={true}/>
<RadixThemesButton type={"submit"}>

{"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c"}
</RadixThemesButton>
</RadixThemesFlex>
</RadixFormRoot>
</RadixThemesBox>
</RadixThemesBox>
<RadixThemesBox css={({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "none" }) })}>

<RadixThemesBox css={({ ["width"] : "95vw" })}>

<RadixFormRoot className={"Root "} css={({ ["width"] : "100%" })} onSubmit={handleSubmit_9a2c705e13b955efed21c41fe61e2381}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"row"} gap={"3"}>

<RadixThemesTextField.Root css={({ ["width"] : "100%" })} name={"title"} placeholder={"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a"} required={true} type={"text"}/>
</RadixThemesFlex>
<RadixThemesTextArea css={({ ["height"] : "50vh", ["width"] : "100%" })} name={"content"} placeholder={"\u0412\u0430\u0448\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435"} required={true}/>
<RadixThemesButton type={"submit"}>

{"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c"}
</RadixThemesButton>
</RadixThemesFlex>
</RadixFormRoot>
</RadixThemesBox>
</RadixThemesBox>
</RadixThemesFlex>
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

<RadixThemesBox css={({ ["background"] : "var(--accent-3)", ["padding"] : "1em", ["width"] : "100%" })} id={"my-main-nav"} ref={ref_my_main_nav}>

<RadixThemesBox css={({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "block" }) })}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center" })} direction={"row"} id={"my-navbar-hstack-desktop"} justify={"between"} ref={ref_my_navbar_hstack_desktop} gap={"3"}>

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

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>

<NextLink href={"/"} passHref={true}>

<RadixThemesText as={"p"} size={"4"} weight={"medium"}>

{"\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430"}
</RadixThemesText>
</NextLink>
</RadixThemesLink>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>

<NextLink href={"/about"} passHref={true}>

<RadixThemesText as={"p"} size={"4"} weight={"medium"}>

{"\u041e \u043d\u0430\u0441"}
</RadixThemesText>
</NextLink>
</RadixThemesLink>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>

<NextLink href={"/articles"} passHref={true}>

<RadixThemesText as={"p"} size={"4"} weight={"medium"}>

{"\u0423\u0440\u043e\u043a\u0438"}
</RadixThemesText>
</NextLink>
</RadixThemesLink>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>

<NextLink href={"/contact"} passHref={true}>

<RadixThemesText as={"p"} size={"4"} weight={"medium"}>

{"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b"}
</RadixThemesText>
</NextLink>
</RadixThemesLink>
</RadixThemesFlex>
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} justify={"end"} gap={"4"}>

<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>

<NextLink href={"/register"} passHref={true}>

<RadixThemesButton size={"3"} variant={"outline"}>

{"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f"}
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })}>

<NextLink href={"/login"} passHref={true}>

<RadixThemesButton size={"3"} variant={"outline"}>

{"\u0412\u0445\u043e\u0434"}
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesBox>
<RadixThemesBox css={({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "none" }) })}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center" })} direction={"row"} justify={"between"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "center" })} direction={"row"} gap={"3"}>

<img css={({ ["width"] : "2em", ["height"] : "auto", ["borderRadius"] : "25%" })} src={"/logo.jpg"}/>
<RadixThemesHeading size={"6"} weight={"bold"}>

{"It-\u043f\u043e\u043b\u0438\u0433\u043e\u043d"}
</RadixThemesHeading>
</RadixThemesFlex>
<RadixThemesDropdownMenu.Root css={({ ["justify"] : "end" })}>

<RadixThemesDropdownMenu.Trigger>

<LucideMenuIcon css={({ ["color"] : "var(--current-color)" })} size={30}/>
</RadixThemesDropdownMenu.Trigger>
<RadixThemesDropdownMenu.Content>

<RadixThemesDropdownMenu.Item onClick={((...args) => (addEvents([(Event("reflex___state____state.prdprf___navigation___state____nav_state.to_home", ({  }), ({  })))], args, ({  }))))}>

{"\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430"}
</RadixThemesDropdownMenu.Item>
<RadixThemesDropdownMenu.Item onClick={((...args) => (addEvents([(Event("reflex___state____state.prdprf___navigation___state____nav_state.to_about_us", ({  }), ({  })))], args, ({  }))))}>

{"\u041e \u043d\u0430\u0441"}
</RadixThemesDropdownMenu.Item>
<RadixThemesDropdownMenu.Item onClick={((...args) => (addEvents([(Event("reflex___state____state.prdprf___navigation___state____nav_state.to_articles", ({  }), ({  })))], args, ({  }))))}>

{"\u0423\u0440\u043e\u043a\u0438"}
</RadixThemesDropdownMenu.Item>
<RadixThemesDropdownMenu.Item onClick={((...args) => (addEvents([(Event("reflex___state____state.prdprf___navigation___state____nav_state.to_contact", ({  }), ({  })))], args, ({  }))))}>

{"Contact"}
</RadixThemesDropdownMenu.Item>
<RadixThemesDropdownMenu.Separator/>
<RadixThemesDropdownMenu.Item onClick={((...args) => (addEvents([(Event("reflex___state____state.prdprf___navigation___state____nav_state.to_login", ({  }), ({  })))], args, ({  }))))}>

{"\u0412\u0445\u043e\u0434"}
</RadixThemesDropdownMenu.Item>
<RadixThemesDropdownMenu.Item onClick={((...args) => (addEvents([(Event("reflex___state____state.prdprf___navigation___state____nav_state.to_register", ({  }), ({  })))], args, ({  }))))}>

{"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f"}
</RadixThemesDropdownMenu.Item>
</RadixThemesDropdownMenu.Content>
</RadixThemesDropdownMenu.Root>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesBox>
<RadixThemesBox css={({ ["padding"] : "1em", ["width"] : "100%" })} id={"my-content-area-el"} ref={ref_my_content_area_el}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["minHeight"] : "95vh" })} direction={"column"} gap={"5"}>

<RadixThemesHeading size={"9"}>

{"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0443\u0440\u043e\u043a"}
</RadixThemesHeading>
<RadixThemesBox css={({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "block" }) })}>

<RadixThemesBox css={({ ["width"] : "50vw" })}>

<RadixFormRoot className={"Root "} css={({ ["width"] : "100%" })} onSubmit={handleSubmit_9a2c705e13b955efed21c41fe61e2381}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"row"} gap={"3"}>

<RadixThemesTextField.Root css={({ ["width"] : "100%" })} name={"title"} placeholder={"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a"} required={true} type={"text"}/>
</RadixThemesFlex>
<RadixThemesTextArea css={({ ["height"] : "50vh", ["width"] : "100%" })} name={"content"} placeholder={"\u0412\u0430\u0448\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435"} required={true}/>
<RadixThemesButton type={"submit"}>

{"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c"}
</RadixThemesButton>
</RadixThemesFlex>
</RadixFormRoot>
</RadixThemesBox>
</RadixThemesBox>
<RadixThemesBox css={({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "none" }) })}>

<RadixThemesBox css={({ ["width"] : "75vw" })}>

<RadixFormRoot className={"Root "} css={({ ["width"] : "100%" })} onSubmit={handleSubmit_9a2c705e13b955efed21c41fe61e2381}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"row"} gap={"3"}>

<RadixThemesTextField.Root css={({ ["width"] : "100%" })} name={"title"} placeholder={"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a"} required={true} type={"text"}/>
</RadixThemesFlex>
<RadixThemesTextArea css={({ ["height"] : "50vh", ["width"] : "100%" })} name={"content"} placeholder={"\u0412\u0430\u0448\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435"} required={true}/>
<RadixThemesButton type={"submit"}>

{"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c"}
</RadixThemesButton>
</RadixThemesFlex>
</RadixFormRoot>
</RadixThemesBox>
</RadixThemesBox>
<RadixThemesBox css={({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "block" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 62em)"] : ({ ["display"] : "none" }) })}>

<RadixThemesBox css={({ ["width"] : "95vw" })}>

<RadixFormRoot className={"Root "} css={({ ["width"] : "100%" })} onSubmit={handleSubmit_9a2c705e13b955efed21c41fe61e2381}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"row"} gap={"3"}>

<RadixThemesTextField.Root css={({ ["width"] : "100%" })} name={"title"} placeholder={"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a"} required={true} type={"text"}/>
</RadixThemesFlex>
<RadixThemesTextArea css={({ ["height"] : "50vh", ["width"] : "100%" })} name={"content"} placeholder={"\u0412\u0430\u0448\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435"} required={true}/>
<RadixThemesButton type={"submit"}>

{"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c"}
</RadixThemesButton>
</RadixThemesFlex>
</RadixFormRoot>
</RadixThemesBox>
</RadixThemesBox>
</RadixThemesFlex>
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
<RadixThemesIconButton css={({ ["padding"] : "6px", ["position"] : "fixed", ["bottom"] : "2rem", ["left"] : "2rem", ["background"] : "transparent", ["color"] : "inherit", ["zIndex"] : "20", ["&:hover"] : ({ ["cursor"] : "pointer" }) })} onClick={toggleColorMode}>

<Fragment>

{isTrue((resolvedColorMode === "light")) ? (
  <Fragment>

<LucideSunIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
) : (
  <Fragment>

<LucideMoonIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
)}
</Fragment>
</RadixThemesIconButton>
</Fragment>
)}
</Fragment>
) : (
  <Fragment>

<RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })}>

<RadixThemesText as={"p"}>

{"Loading..."}
</RadixThemesText>
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

export default function Component() {
    




  return (
    <Errorboundary_50c24ff147beb0d8cf78317c90541a63/>
  )
}
