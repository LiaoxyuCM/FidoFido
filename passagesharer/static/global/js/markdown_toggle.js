const getQueryParam = (name) => {
    const params = new URLSearchParams(window.location.search);
    return params.get(name);
};

document.addEventListener("DOMContentLoaded", () => {
    const markdownToggle = document.querySelector("a.markdown_toggle");
    markdownToggle.setAttribute("href", getQueryParam("markdown") === "on" ? "?markdown=off" : "?markdown=on");
    const markdownToggleTextContent = markdownToggle.querySelector("button.markdown_toggle_button");
    markdownToggleTextContent.innerHTML = getQueryParam("markdown") === "on" ? "*M*" : "<i>M</i>";
});
