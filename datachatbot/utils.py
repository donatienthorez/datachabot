
class Utils:

    def format_sources(sources):
        formatted_sources = []
        for index, source in enumerate(sources, start=1):
            page_content = source.page_content
            metadata_source = source.metadata['source']
            formatted_source = f"Source {index}. {page_content} from **{metadata_source}** \n"
            formatted_sources.append(formatted_source)
        formatted_sources_text = '\n'.join(formatted_sources)

        return formatted_sources_text


    def format_response(response, sources):
        formatted_sources_text = Utils.format_sources(sources)
        return f"""
                {response}    
                &mdash;   
                {formatted_sources_text}
            """