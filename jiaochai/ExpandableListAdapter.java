public class ExpandableListAdapter extends BaseExpandableListAdapter {

    private Context mContext;
    private ArrayList<String> mHeaderData;
    private HashMap<String, List<String>> mChildData;

    public ExpandableListAdapter(Context context,
                                 ArrayList<String> headerData,
                                 HashMap<String, List<String>> childData) {
        mContext = context;
        mHeaderData = headerData;
        mChildData = childData;
    }

    @Override
    public int getGroupCount() {
        return mHeaderData.size();
    }

    @Override
    public int getChildrenCount(int groupPosition) {
        return mChildData.get(mHeaderData.get(groupPosition)).size();
    }

    @Override
    public Object getGroup(int groupPosition) {
        return mHeaderData.get(groupPosition);
    }

    @Override
    public Object getChild(int groupPosition, int childPosition) {
        return mChildData.get(mHeaderData.get(groupPosition)).get(childPosition);
    }

    @Override
    public long getGroupId(int groupPosition) {
        return groupPosition;
    }

    @Override
    public long getChildId(int groupPosition, int childPosition) {
        return childPosition;
    }

    @Override
    public boolean hasStableIds() {
        return false;
    }

    @Override
    public View getGroupView(int groupPosition, boolean isExpanded, View convertView, ViewGroup parent) {
        String headerTitle = (String) getGroup(groupPosition);

        if (convertView == null) {
            LayoutInflater inflater = (LayoutInflater) mContext.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.list_group, null);
        }

        TextView headerTextView = convertView.findViewById(R.id.header_text_view);
        headerTextView.setText(headerTitle);

        ImageView headerImageView = convertView.findViewById(R.id.header_image_view);
        if(isExpanded) {
            headerImageView.setImageResource(R.drawable.ic_arrow_up);
        } else {
            headerImageView.setImageResource(R.drawable.ic_arrow_down);
        }

        return convertView;
    }

    @Override
    public View getChildView(int groupPosition, int childPosition, boolean isLastChild, View convertView, ViewGroup parent) {
        String childTitle = (String) getChild(groupPosition, childPosition);

        if (convertView == null) {
            LayoutInflater inflater = (LayoutInflater) mContext.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.list_item, null);
        }

        TextView childTextView = convertView.findViewById(R.id.item_text_view);
        childTextView.setText(childTitle);

        return convertView;
    }

    @Override
    public boolean isChildSelectable(int groupPosition, int childPosition) {
        return true;
    }
}