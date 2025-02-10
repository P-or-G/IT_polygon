/** @jsxImportSource @emotion/react */


import { ErrorBoundary } from "react-error-boundary"
import { Fragment, useCallback, useContext, useEffect, useRef, useState } from "react"
import { ColorModeContext, EventLoopContext, StateContexts } from "$/utils/context"
import { Event, getBackendURL, getRefValue, getRefValues, isTrue, refs } from "$/utils/state"
import { jsx, keyframes } from "@emotion/react"
import { TriangleAlertIcon as LucideTriangleAlertIcon, WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { toast, Toaster } from "sonner"
import env from "$/env.json"
import { Button as RadixThemesButton, Callout as RadixThemesCallout, Card as RadixThemesCard, Flex as RadixThemesFlex, Heading as RadixThemesHeading, Link as RadixThemesLink, Select as RadixThemesSelect, Text as RadixThemesText, TextField as RadixThemesTextField } from "@radix-ui/themes"
import { GoogleLogin, GoogleOAuthProvider } from "@react-oauth/google"
import { Root as RadixFormRoot } from "@radix-ui/react-form"
import NextLink from "next/link"
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

export function Div_602c14884fa2de27f522fe8f94374b02 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    <div css={({ ["position"] : "fixed", ["width"] : "100vw", ["height"] : "0" })} title={("Connection Error: "+((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''))}>

<Fragment_f2f0916d2fcc08b7cdf76cec697f0750/>
</div>
  )
}

export function Fragment_c1c8251bf583dc2bb103b4315a228be0 () {
  
  const reflex___state____state__reflex_local_auth___local_auth____local_auth_state__reflex_local_auth___registration____registration_state = useContext(StateContexts.reflex___state____state__reflex_local_auth___local_auth____local_auth_state__reflex_local_auth___registration____registration_state)
  const reflex___state____state__prdprf___auth___state____select_class_state = useContext(StateContexts.reflex___state____state__prdprf___auth___state____select_class_state)
  const reflex___state____state__prdprf___auth___state____select_litera_state = useContext(StateContexts.reflex___state____state__prdprf___auth___state____select_litera_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);
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
  )
}

export function Errorboundary_01376200c27cbdb1b20bd5c326893fe8 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_error_0f5dbf674521530422d73a7946faf6d4 = useCallback(((_error, _info) => (addEvents([(Event("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception", ({ ["stack"] : _error["stack"], ["component_stack"] : _info["componentStack"] }), ({  })))], [_error, _info], ({  })))), [addEvents, Event])



  
  return (
    <ErrorBoundary fallbackRender={((event_args) => (jsx("div", ({ ["css"] : ({ ["height"] : "100%", ["width"] : "100%", ["position"] : "absolute", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" }) }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "1rem" }) }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "1rem", ["maxWidth"] : "50ch", ["border"] : "1px solid #888888", ["borderRadius"] : "0.25rem", ["padding"] : "1rem" }) }), (jsx("h2", ({ ["css"] : ({ ["fontSize"] : "1.25rem", ["fontWeight"] : "bold" }) }), (jsx(Fragment, ({  }), "An error occurred while rendering this page.")))), (jsx("p", ({ ["css"] : ({ ["opacity"] : "0.75" }) }), (jsx(Fragment, ({  }), "This is an error with the application itself.")))), (jsx("details", ({  }), (jsx("summary", ({ ["css"] : ({ ["padding"] : "0.5rem" }) }), (jsx(Fragment, ({  }), "Error message")))), (jsx("div", ({ ["css"] : ({ ["width"] : "100%", ["maxHeight"] : "50vh", ["overflow"] : "auto", ["background"] : "#000", ["color"] : "#fff", ["borderRadius"] : "0.25rem" }) }), (jsx("div", ({ ["css"] : ({ ["padding"] : "0.5rem", ["width"] : "fit-content" }) }), (jsx("pre", ({  }), (jsx(Fragment, ({  }), event_args.error.stack)))))))), (jsx("button", ({ ["css"] : ({ ["padding"] : "0.35rem 0.75rem", ["margin"] : "0.5rem", ["background"] : "#fff", ["color"] : "#000", ["border"] : "1px solid #000", ["borderRadius"] : "0.25rem", ["fontWeight"] : "bold" }), ["onClick"] : ((...args) => (addEvents([(Event("_call_function", ({ ["function"] : (() => (navigator["clipboard"]["writeText"](event_args.error.stack))), ["callback"] : null }), ({  })))], args, ({  })))) }), (jsx(Fragment, ({  }), "Copy")))))))), (jsx("hr", ({ ["css"] : ({ ["borderColor"] : "currentColor", ["opacity"] : "0.25" }) }))), (jsx("a", ({ ["href"] : "https://reflex.dev" }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["alignItems"] : "baseline", ["justifyContent"] : "center", ["fontFamily"] : "monospace", ["--default-font-family"] : "monospace", ["gap"] : "0.5rem" }) }), (jsx(Fragment, ({  }), "Built with ")), (jsx("svg", ({ ["css"] : ({ ["viewBox"] : "0 0 56 12", ["fill"] : "currentColor" }), ["height"] : "12", ["width"] : "56", ["xmlns"] : "http://www.w3.org/2000/svg" }), (jsx("path", ({ ["d"] : "M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z" }))), (jsx("path", ({ ["d"] : "M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z" }))), (jsx("path", ({ ["d"] : "M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z" }))), (jsx("path", ({ ["d"] : "M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z" }))), (jsx("path", ({ ["d"] : "M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z" }))), (jsx("path", ({ ["d"] : "M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z" }))))))))))))))} onError={on_error_0f5dbf674521530422d73a7946faf6d4}>

<Fragment>

<Div_602c14884fa2de27f522fe8f94374b02/>
<Toaster_6e6ebf8d7ce589d59b7d382fb7576edf/>
</Fragment>
<RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "85vh" })}>

<Fragment_c1c8251bf583dc2bb103b4315a228be0/>
</RadixThemesFlex>
<NextHead>

<title>

{"Register"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</ErrorBoundary>
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
    <Errorboundary_01376200c27cbdb1b20bd5c326893fe8/>
  )
}
